import paho.mqtt.client as mqtt
import OSC
import json
import time

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("track")
	client.subscribe("lasers")

TRESH = 50
count_laser1 = 0
count_laser0 = 0
value_laser1 = 0
value_laser0 = 0

def on_message(client, userdata, msg):
        global count_laser0, count_laser1, value_laser0, value_laser1

        parsedMsg = json.loads(msg.payload)
        oscMessage = OSC.OSCMessage()
        oscMessage.setAddress("/" + parsedMsg["elemid"])
        address = parsedMsg["elemid"]
        value = 0
	print("1")

        if address.startswith("laser0"):
            value = value_laser0

            if float(parsedMsg["value"]) > .1:
                value = 1
                count_laser0 = 0
            else:
                count_laser0 += 1

                if count_laser0 > TRESH:
                    value = 0

            value_laser0 = value

        elif address.startswith("laser1"):
            value = value_laser1

            if float(parsedMsg["value"]) > .3:
                value = 1
                count_laser1 = 0
            else:
                count_laser1 += 1

                if count_laser1 > TRESH:
                    value = 0

            value_laser1 = value

        else:
            value = parsedMsg["value"]

        oscMessage.append(float(value))
        print(oscMessage)
	print("test")
        oscClient.send(oscMessage)

mqttClient = mqtt.Client()
mqttClient.on_connect = on_connect
mqttClient.on_message = on_message
mqttClient.connect("localhost", 1883, 60)

#oscClient = OSC.OSCClient()
#oscClient.connect(("192.168.178.22", 9999))

mqttClient.loop_forever()
