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
#    mqttClient.subscribe("examples")
    mqttClient.subscribe("dwm/node/db8e/uplink/location")



def on_message(client, userdata, msg):
    parsedMsg = json.loads(str(msg.payload.decode("utf-8", "ignore")))
    #print(parsedMsg)
    #datei.write("\n" + parsedMsg)
    sensorName = str(parsedMsg["position"].keys())
    print(sensorName)

mqttClient = mqtt.Client()
mqttClient.on_connect = on_connect
mqttClient.on_message = on_message
mqttClient.connect("localhost", 1883, 60)
mqttClient.loop_forever()
