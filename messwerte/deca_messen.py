import paho.mqtt.client as mqtt
import os
import json

#if os.path.exists("trackingdaten.txt"):
#  os.remove("trackingdaten.txt")
#else:
#  print("The file does not exist") 


datei = open('decadaten.txt','w')
#datei.write("start")

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    mqttClient.subscribe("dwm/node/db8e/uplink/location")



def on_message(client, userdata, msg):
    parsedMsg = json.loads(msg.payload.decode("utf-8", "ignore"))
#    print(parsedMsg)
    #datei.write("\n" + parsedMsg)
    zahl = [0, 0, 0]
    zahl[0] = str(parsedMsg["position"]["y"] - 0.83)
    zahl[1] = str(parsedMsg["position"]["x"] - 1.01)
    zahl[2] = str(parsedMsg["position"]["z"] - 0.43)
#    print(zahl)
    datei.write("\n" + zahl[0] + ";" + zahl[1] + ";" + zahl[2])
    print(zahl[0] + ";" + zahl[1] + ";" + zahl[2])

mqttClient = mqtt.Client()
mqttClient.on_connect = on_connect
mqttClient.on_message = on_message
mqttClient.connect("localhost", 1883, 60)
mqttClient.loop_forever()
