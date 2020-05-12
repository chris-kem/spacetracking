Spacetracking - RTLS for dance performances
===========================================

 ....

## Running

 On a linux system with all dependencies installed, you can execute the serve.sh script:

    ./serve.sh
    Sun, 05 Jan 2020 14:34:34 +0100 | INFO   | server     |  | Serving from directory      : /home/phil/src/spacetracking/wsbin
    Sun, 05 Jan 2020 14:34:34 +0100 | INFO   | server     |  | Serving static content from : html
    Sun, 05 Jan 2020 14:34:34 +0100 | INFO   | server     |  | Starting WebSocket server   : ws://pluto:8080/
    Sun, 05 Jan 2020 14:34:34 +0100 | INFO   | server     |  | Serving CGI or static files : http://pluto:8080/

 Afterwards point your browser to [http://localhost:8080/index.html](http://localhost:8080/index.html).

## Dependencies

 - mosquitto
 - https://github.com/mqttjs/MQTT.js
