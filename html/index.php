<!DOCTYPE html>
<html class="no-js" lang="">

<head>
  <meta charset="utf-8" />
  <title>Positionsdaten</title>
  <meta name="description" content="" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />

  <link rel="manifest" href="site.webmanifest" />
  <link rel="apple-touch-icon" href="icon.png" />
  <!-- Place favicon.ico in the root directory -->

  <link rel="stylesheet" href="css/normalize.css" />
  <link rel="stylesheet" href="css/main.css" />
  <link rel="stylesheet" type="text/css" href="css/style.css" />

  <link rel="stylesheet" href="jquery/jquery.mobile-1.4.5.min.css" />


</head>

<body>
  <div id="page" data-role="page" data-theme="b">
    <!------------------------------------Sensordaten----------------- -->
    <div class="header" data-role="header">
      <h1>Sensordaten</h1>
    </div>
    <div class="flex">
      <div class="sensorX">
        <form>
          <h3 for="textfeld1">Sensor 1</h3>
          <input id="textfeld1" readonly />
        </form>
        <label for="dropdown1">Wählen Sie eine Funktion:
          <select name="dropdown1" id="dropdown1" class="dropdown">
            <option value="linear1">Linear</option>
            <option value="binär1">Binär</option>
            <option value="harfe1">Harfe</option>
          </select>
        </label>
        <fieldset id="schwelle1" class="schwellenwert">
          <label for="groesse1">Schwellenwert:</label>
          <input id="groesse1" type="number" min="0" max="1" step=".05" value=".2" />
        </fieldset>
        <fieldset class="toggle">
          <label for="flip-1">Wert halten:</label>
          <select onchange="changeTheme()" name="flip-1" id="flip-1" data-role="slider">
            <option value="off">Off</option>
            <option value="on">On</option>
          </select>
        </fieldset>
      </div>

      <div class="sensorX">
        <form>
          <h3 for="textfeld2">Sensor 2</h3>
          <input id="textfeld2" readonly />
        </form>
        <label for="dropdown2">Wählen Sie eine Funktion:
          <select name="dropdown2" id="dropdown2" class="dropdown">
            <option value="linear2">Linear</option>
            <option value="binär2">Binär</option>
            <option value="harfe2">Harfe</option>
          </select>
        </label>
        <fieldset id="schwelle2" class="schwellenwert">
          <label for="groesse2">Schwellenwert:<input id="groesse2" type="number" min="0" max="1" step=".05"
              value=".2" /></label>
        </fieldset>
        <fieldset class="toggle">
          <label for="flip-2">Wert halten:</label>
          <select name="flip-2" id="flip-2" data-role="slider">
            <option value="off">Off</option>
            <option value="on">On</option>
          </select>
        </fieldset>
      </div>

      <div class="sensorX">
        <form>
          <h3 for="textfeld3">Sensor 3</h3>
          <input id="textfeld3" readonly />
        </form>
        <label for="dropdown3">Wählen Sie eine Funktion:
          <select name="dropdown3" id="dropdown3" class="dropdown">
            <option value="linear3">Linear</option>
            <option value="binär3">Binär</option>
            <option value="harfe3">Harfe</option>
          </select>
        </label>
        <fieldset id="schwelle3" class="schwellenwert">
          <label for="groesse3">Schwellenwert:<input id="groesse3" type="number" min="0" max="1" step=".05"
              value=".2" /></label>
        </fieldset>
        <fieldset class="toggle">
          <label for="flip-3">Wert halten:</label>
          <select name="flip-3" id="flip-3" data-role="slider">
            <option value="off">Off</option>
            <option value="on">On</option>
          </select>
        </fieldset>
      </div>

      <div class="sensorX">
        <form>
          <h3 for="textfeld4">Sensor 4</h3>
          <input id="textfeld4" readonly />
        </form>
        <label for="dropdown4">Wählen Sie eine Funktion:
          <select name="dropdown4" id="dropdown4" class="dropdown">
            <option value="linear4">Linear</option>
            <option value="binär4">Binär</option>
            <option value="harfe4">Harfe</option>
          </select>
        </label>
        <fieldset id="schwelle4" class="schwellenwert">
          <label for="groesse4">Schwellenwert:<input id="groesse4" type="number" min="0" max="1" step=".05"
              value=".2" /></label>
        </fieldset>
        <fieldset class="toggle">
          <label for="flip-4">Wert halten:</label>
          <select name="flip-4" id="flip-4" data-role="slider">
            <option value="off">Off</option>
            <option value="on">On</option>
          </select>
        </fieldset>
      </div>
    </div>
    <!------------------------------------Positiontracker----------------- -->
    <div class="tracking">
      <div class="header" data-role="header">
        <h1 class="header">Positionsbestimmung</h1>
      </div>
      <!-- define which picture as floorplan--------type="image/svg+xml"--------- -->
      <div id="svg">
        <object id="dataSVG" data="uploads/Zeichnung.svg" type="image/svg+xml"></object>
      </div>

      <!-- Datei Upload -->
      <div class="upload">
        <form action="download.php" method="post" enctype="multipart/form-data">
          Wählen Sie eine .svg Datei zum Hochladen:
          <input type="file" name="fileToUpload" id="fileToUpload" />
          <input type="submit" value="Hochladen" name="submit" />
        </form>
        </br>
        <form>
          <label for="whichFile">Welche der hochgeladenen Dateien soll dargestellt werden?:</label><input
            name="whichFile" id="whichFile" />
          <button onclick="changeSVG()" type="button" name="submit1">
            Auswählen
          </button>
        </form>
      </div>
    </div>
  </div>
  <!--end page>
    <!--[if IE]>
      <p class="browserupgrade">
        You are using an <strong>outdated</strong> browser. Please
        <a href="https://browsehappy.com/">upgrade your browser</a> to improve
        your experience and security.
      </p>
    <![endif]-->

  <!-- Add your site or application content here -->

  <!-- Google Analytics: change UA-XXXXX-Y to be your site's ID.
  <script>
    window.ga = function () { ga.q.push(arguments) }; ga.q = []; ga.l = +new Date;
    ga('create', 'UA-XXXXX-Y', 'auto'); ga('set','transport','beacon'); ga('send', 'pageview')
  </script>
  <script src="https://www.google-analytics.com/analytics.js" async></script>
  -->

  <script src="jquery/jquery.js"></script>
  <script src="jquery/jquery.mobile-1.4.5.min.js"></script>
  <script src="js/vendor/modernizr-3.7.1.min.js"></script>
  <script src="https://code.jquery.com/jquery-3.4.1.min.js"
    integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin="anonymous"></script>
  <script>
    window.jQuery ||
      document.write(
        '<script src="js/vendor/jquery-3.4.1.min.js"><\/script>'
      );
  </script>
  <script src="js/plugins.js"></script>
  <script src="js/main.js"></script>
  <script src="js/mqtt.js"></script>

  <script>
    function changeSVG() {
      document.getElementById("dataSVG").data = document.getElementById(
        "whichFile"
      ).value;
    }

    var binary_Val1_t = JSON.stringify({
      Sensor0: 1
    });
    var binary_Val1_f = JSON.stringify({
      Sensor0: 0
    });
    var binary_Val2_t = JSON.stringify({
      Sensor1: 1
    });
    var binary_Val2_f = JSON.stringify({
      Sensor1: 0
    });
    var binary_Val3_t = JSON.stringify({
      Sensor2: 1
    });
    var binary_Val3_f = JSON.stringify({
      Sensor2: 0
    });
    var binary_Val4_t = JSON.stringify({
      Sensor3: 1
    });
    var binary_Val4_f = JSON.stringify({
      Sensor3: 0
    });

    document.getElementById("textfeld1").value = "";
    document.getElementById("textfeld2").value = "";
    document.getElementById("textfeld3").value = "";
    document.getElementById("textfeld4").value = "";

    // Create a client instance
    var client = mqtt.connect(
      location.origin.replace(location.protocol, "ws:") + ":15675"
    );
    client.on("connect", function () {
      client.subscribe("lasers/#");
    });
    //what to do when receiving a mqtt message
    client.on("message", function (topic, msg) {
      var x = JSON.parse(msg);
      //--------------------linear and laserx-------------------------------------
      if (
        document.getElementById("dropdown1").value == "linear1" &&
        topic == "lasers/linear/laser0"
      ) {
        document.getElementById("textfeld1").value = x;
        //publish to mqtt topic which sends data via OSC
        var toSend = JSON.stringify({
          Sensor0: x
        })
        client.publish("lasers/OSC/laser0", toSend);
      } else if (
        document.getElementById("dropdown2").value == "linear2" &&
        topic == "lasers/linear/laser1"
      ) {
        newtext2 = document.getElementById("textfeld2").value;
        document.getElementById("textfeld2").value = msg;
        client.publish("lasers/OSC/laser1", msg);
      } else if (
        document.getElementById("dropdown3").value == "linear3" &&
        topic == "lasers/linear/laser2"
      ) {
        newtext3 = document.getElementById("textfeld3").value;
        document.getElementById("textfeld3").value = msg;
        client.publish("lasers/OSC/laser2", msg);
      } else if (
        document.getElementById("dropdown4").value == "linear4" &&
        topic == "lasers/linear/laser3"
      ) {
        newtext4 = document.getElementById("textfeld4").value;
        document.getElementById("textfeld4").value = msg;
        client.publish("lasers/OSC/laser3", msg);

        //-------------------------------binary and laserx--------------------------------------------------
      } else if (
        document.getElementById("dropdown1").value == "binär1" &&
        topic == "lasers/linear/laser0"
      ) {
        if (x > document.getElementById("groesse1").value) {
          document.getElementById("textfeld1").value = "1";
          client.publish("lasers/OSC/laser0", JSON.stringify({
            Sensor0: 1
          }));
        } else {
          document.getElementById("textfeld1").value = "0";
          client.publish("lasers/OSC/laser0", JSON.stringify({
            Sensor0: 0
          }));
        }
      } else if (
        document.getElementById("dropdown2").value == "binär2" &&
        topic == "lasers/linear/laser1"
      ) {
        if (x > document.getElementById("groesse2").value) {
          document.getElementById("textfeld2").value = "1";
          client.publish("lasers/OSC/laser1", JSON.stringify({
            Sensor1: 1
          }));
        } else {
          document.getElementById("textfeld2").value = "0";
          client.publish("lasers/OSC/laser1", JSON.stringify({
            Sensor1: 0
          }));
        }
      } else if (
        document.getElementById("dropdown3").value == "binär3" &&
        topic == "lasers/linear/laser2"
      ) {
        if (x > document.getElementById("groesse3").value) {
          document.getElementById("textfeld3").value = "1";
          client.publish("lasers/OSC/laser2", JSON.stringify({
            Sensor2: 1
          }));
        } else {
          document.getElementById("textfeld3").value = "0";
          client.publish("lasers/OSC/laser2", JSON.stringify({
            Sensor2: 0
          }));
        }
      } else if (
        document.getElementById("dropdown4").value == "binär4" &&
        topic == "lasers/linear/laser3"
      ) {
        if (x > document.getElementById("groesse4").value) {
          document.getElementById("textfeld4").value = "1";
          client.publish("lasers/OSC/laser3", JSON.stringify({
            Sensor3: 1
          }));
        } else {
          document.getElementById("textfeld4").value = "0";
          client.publish("lasers/OSC/laser3", JSON.stringify({
            Sensor3: 0
          }));
        }

        //---------------------------------harfe and laserx----------------------------------------------------
      } else if (
        document.getElementById("dropdown1").value == "harfe1" &&
        topic == "lasers/harfe/laser0"
      ) {
        newtext1 = document.getElementById("textfeld1").value;
        document.getElementById("textfeld1").value = msg;
        client.publish("lasers/OSC/laser0", msg);
      } else if (
        document.getElementById("dropdown2").value == "harfe2" &&
        topic == "lasers/harfe/laser1"
      ) {
        newtext2 = document.getElementById("textfeld2").value;
        document.getElementById("textfeld2").value = msg;
        client.publish("lasers/OSC/laser1", msg);
      } else if (
        document.getElementById("dropdown3").value == "harfe3" &&
        topic == "lasers/harfe/laser2"
      ) {
        newtext3 = document.getElementById("textfeld3").value;
        document.getElementById("textfeld3").value = msg;
        client.publish("lasers/OSC/laser2", msg);
      } else if (
        document.getElementById("dropdown4").value == "harfe4" &&
        topic == "lasers/harfe/laser3"
      ) {
        newtext4 = document.getElementById("textfeld4").value;
        document.getElementById("textfeld4").value = msg;
        client.publish("lasers/OSC/laser3", msg);
      }
    });
  </script>

  <script src="js/spacetracking.js"></script>
</body>

</html>