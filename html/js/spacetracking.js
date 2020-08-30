//
// spacetracker.js - retrieve RTLS position via MQTT, lowpass filter, and do
// hit-testing on an SVG floorplan. On hit, publish the grayscale value of the
// position found in the SVG togehter with the id of the hit object.
//
// All elements on that have an id starting with "track" will be tracked!
//

//
// get the SVG for hit-testing, and render on a canvas for color retrieval
//
$(document).ready(function () {

  //while (document.getElementById("dataSVG").value == "undefined" || "null") {
  //setTimeout(console.log("kein SVG zum tracken verfügbar"), 1000);
  //}

  var root = document.getElementById('dataSVG');
  //if (typeof root !== 'undefined' && root !== null) {
  var doc = root.contentDocument;
  //}
  //if (typeof doc !== 'undefined' && doc !== null) {
  var svg = doc.activeElement;
  //var svg = doc.documentElement;
  //} if (typeof svg !== 'undefined' && svg !== null) {
  var can = document.createElement('canvas');
  //);

  //
  // only track the track- element
  //
  var t = svg.querySelectorAll('[id^="track"]'),
    tracked = {};
  t.forEach(function (x) { tracked[x.id] = 0 })

  if (tracked.length == 0)
    console.log("WARN: no tracked elements, please add elements to svg with an id 'track'");

  //
  // this is the size of the actual svg
  //
  can.width = svg.width.baseVal.valueInSpecifiedUnits;
  can.height = svg.height.baseVal.valueInSpecifiedUnits;

  //
  // draw the image on a canvas to retrieve color values at a position
  // XXX this could get problematic for large svgs
  //
  var ctx = can.getContext('2d'),
    img = new Image();
  img.onload = function () { ctx.drawImage(img, 0, 0, can.width, can.height); }
  img.src = root.data; // get data from containing <object>


  //
  // we do lowpass-filtering according to the Decawave implementation.
  //
  CONSTANT = 10; TAGPOS = {};
  function lowpass(cur, now) {
    return (CONSTANT * cur + now) / (CONSTANT + 1);
  }
  //------------------});
  //
  // connect to the MQTT broker and subscribe to all locations updates from
  // all nodes in the network.
  //
  var client = mqtt.connect(location.origin.replace(location.protocol, 'ws:') + ":15675");
  //var client = mqtt.connect("ws://spacetracker.local:15675/ws");

  client.on('connect', function () { client.subscribe('dwm/node/+/uplink/location'); });
  client.on('message', function (topic, msg) {
    //console.log(topic);
    var pos = JSON.parse(msg.toString()).position,
      point = svg.createSVGPoint(),
      marcer = svg.getElementById('tag'),
      tagid = topic.split('/')[2];

    //
    // convert to SVG coordinate systems, SVGs coordinate systems are bottom left,
    // while the coordinate axis of the brower is rooted in the top left corner.
    //
    pos.x = parseFloat(pos.x) * 1000;
    pos.y = can.height - parseFloat(pos.y) * 1000;
    //pos.y = parseFloat(pos.y) * 100;
    //console.log(pos.x + ", " + pos.y);

    //
    // check if we received a valid position
    //
    if (Number.isNaN(pos.x) || Number.isNaN(pos.y))
      return;

    if (parseFloat(pos.quality) < 50)
      return;

    //
    // quickfix for being off-scale
    //
    // pos.x += 526;
    // pos.y -= 756;

    //
    // low-pass filter the positions.
    //
    if (TAGPOS[tagid] == undefined) {
      TAGPOS[tagid] = pos;
    }

    pos.x = lowpass(TAGPOS[tagid].x, pos.x);
    pos.y = lowpass(TAGPOS[tagid].y, pos.y);

    TAGPOS[tagid] = pos;

    //
    // for debugging and interaction
    //
    point.x = pos.x; point.y = pos.y;
    point = point.matrixTransform(svg.getTransformToElement(marcer));
    if (marcer) {
      marcer.setAttribute('cx', point.x);
      marcer.setAttribute('cy', point.y);
    }
    //
    // hit-test on SVG element, disable the display of the tag element briefly,
    // otherwise it is on top.
    //
    point.x = pos.x; point.y = pos.y;
    point = point.matrixTransform(svg.getScreenCTM());

    //var xyz = point.x.toString() + point.y.toString();

    marcer.setAttribute('visibility', 'hidden');
    var el = doc.elementFromPoint(point.x, point.y);
    marcer.setAttribute('visibility', '');

    for (i in tracked) { tracked[i] = 0.; }

    if (el != null && el.id.startsWith('track')) {
      //
      // got a hit -> get its color from the canvas
      // convert to grayscale based on
      // https://www.johndcook.com/blog/2009/08/24/algorithms-convert-color-grayscale/
      //
      point.x = pos.x; point.y = pos.y;
      //var ctx = tracked[el.id].getContext("2d");
      var c = ctx.getImageData(point.x, point.y, 1, 1).data;
      //console.log(el.style);
      //tracked[el.id] = (c[3]/255.) - (0.21*c[0] + 0.72*c[1] + 0.07*c[2])/255;
      //tracked[el.id] = (0.21*c[0] + 0.72*c[1] + 0.07*c[2])/255;
      tracked[el.id] = (c[3] / 255.);
      //tracked[el.id] = 1 - 0.21*c[0] + 0.72*c[1] + 0.07*c[2];
      //console.log(c[0] + ", " + c[0] + ", " + c[1] + ", " + c[2] + ", " + c[3]);
      //console.log(tracked[el.id]);
    }

    client.publish('decadaten', (pos.x / 1000) + "; " + (pos.y / 1000));

    var o = new Object();
    o.nodeid = pos.nodeid;

    for (i in tracked) {
      o.elemid = i;
      o.value = tracked[i];
      client.publish('track', JSON.stringify(o));
    }
  });
});
//
