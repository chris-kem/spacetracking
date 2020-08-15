import paho.mqtt.client as mqtt
import os

#if os.path.exists("trackingdaten.txt"):
#  os.remove("trackingdaten.txt")
#else:
#  print("The file does not exist") 


datei = open('trackingdaten.txt','w')
#datei.write("start")

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    mqttClient.subscribe("examples")
#    mqttClient.subscribe("dwm/node/ViveTracker/uplink/location")



def on_message(client, userdata, msg):
    parsedMsg = str(msg.payload.decode("utf-8", "ignore"))
    print(parsedMsg)
    datei.write(parsedMsg)


mqttClient = mqtt.Client()
mqttClient.on_connect = on_connect
mqttClient.on_message = on_message
mqttClient.connect("localhost", 1883, 60)
mqttClient.loop_forever()
