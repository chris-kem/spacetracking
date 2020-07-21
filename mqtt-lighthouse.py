import paho.mqtt.client as mqtt
import cgi
import json
import time


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    mqttClient.subscribe("examples")


def on_message(client, userdata, msg):
    #	print(str(msg.payload))
    #	print(msg.payload.decode("utf-8","ignore"))
    parsedMsg = str(msg.payload.decode("utf-8", "ignore"))
#    print(parsedMsg)
    zahl = ["0", "0", "0"]
    i = 0
    for word in parsedMsg.split(";", 2):
        zahl[i] = float(word)
        i += 1

#    print(zahl[0] + " "+zahl[1] + " "+zahl[2])
    message_out = {"x": zahl[0], "y": zahl[1], "z": zahl[2]}
#    print(message_out)
    data_out = json.dumps(message_out)
#    print(data_out)
    mqttClient.publish("dwm/node/ViveTracker/uplink/location", data_out)


mqttClient = mqtt.Client()
mqttClient.on_connect = on_connect
mqttClient.on_message = on_message
mqttClient.connect("localhost", 1883, 60)
mqttClient.loop_forever()
