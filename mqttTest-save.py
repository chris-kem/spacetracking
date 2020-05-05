import paho.mqtt.client as mqtt
import OSC
import json
import time

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("track")
	client.subscribe("lasers")

#loloolololo

def on_message(client, userdata, msg):
	tpc = msg.topic
	if tpc.endswith("track") or tpc.endswith("lasers"):
		parsedMsg = json.loads(msg.payload)
		oscMessage = OSC.OSCMessage()
		oscMessage.setAddress("/" + parsedMsg["elemid"])
		address = parsedMsg["elemid"]
		value = 0
		if address.startswith("laser0") or address.startswith("laser1"):
			if float(parsedMsg["value"]) > .1:
				value = 1
		else:
			value = parsedMsg["value"]
		oscMessage.append(float(value))
		print(oscMessage)
		oscClient.send(oscMessage)

mqttClient = mqtt.Client()
mqttClient.on_connect = on_connect
mqttClient.on_message = on_message
mqttClient.connect("localhost", 1883, 60)

oscClient = OSC.OSCClient()
oscClient.connect(("192.168.1.6", 8001))

mqttClient.loop_forever()
