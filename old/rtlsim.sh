while true;
do echo '{ "x": 12, "y": 13 }';
sleep 1;
done | mosquitto_pub -t dwm/node/abc3/uplink/location -l

