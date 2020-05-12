#!/bin/bash

trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT

mosquitto -c mosquitto.conf -v &
sleep  10
./rtlsim | mosquitto_pub -t rtls -l &
chromium-browser http://localhost:9001/index.html
sleep infinity
