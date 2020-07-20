import paho.mqtt.client as mqtt
import cgi
import json
import time

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	mqttClient.subscribe("examples")

def on_message(client, userdata, msg):
	#print(msg)
	parsedMsg = json.loads(str(msg.payload.decode("utf-8","ignore")))
	print(parsedMsg)
	for word in parsedMsg.split(";", 3):
		zahl = float(word)
		print(zahl)
        	#else:
	    	#	mqttClient.publish("errors", value)
	    	#	print("error %d" + value)

       # print(value)

mqttClient = mqtt.Client()
mqttClient.on_connect = on_connect
mqttClient.on_message = on_message
mqttClient.connect("localhost", 1883, 60)
mqttClient.loop_forever()
