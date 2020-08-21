import paho.mqtt.client as mqtt
import os
import json
import sys
import time

# if os.path.exists("trackingdaten.txt"):
#  os.remove("trackingdaten.txt")
# else:
#  print("The file does not exist")


datei = open('decadaten.txt', 'w')
# datei.write("start")

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    mqttClient.subscribe("decadaten")
#    mqttClient.subscribe("dwm/node/db8e/uplink/location")


start = time.time()
while True:
    try:
        def on_message(client, userdata, msg):
            parsedMsg = msg.payload.decode("utf-8", "ignore")
#    print(parsedMsg)
    #datei.write("\n" + parsedMsg)
#    zahl = [0, 0]
#    zahl[0] = str(parsedMsg["position"]["x"])
#    zahl[1] = str(parsedMsg["position"]["y"])
#    zahl[2] = str(parsedMsg["position"]["z"] - 0.43)
#    print(zahl)
            datei.write("\n" + parsedMsg)
            print(parsedMsg)

        mqttClient = mqtt.Client()
        mqttClient.on_connect = on_connect
        mqttClient.on_message = on_message
        mqttClient.connect("localhost", 1883, 60)
        mqttClient.loop_forever()

    except KeyboardInterrupt:
        end = time.time()
        print(end - start)
        sys.exit()
