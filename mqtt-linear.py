import paho.mqtt.client as mqtt
import json
import time

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	mqttClient.subscribe("lasers/raw/#")

TRESH = 50
count_laser1 = 0
count_laser0 = 0
count_laser2 = 0
count_laser3 = 0
value_laser1 = 0
value_laser0 = 0
value_laser2 = 0
value_laser3 = 0

def on_message(client, userdata, msg):
        global count_laser0, count_laser1, value_laser0, value_laser1, count_laser2, count_laser3, value_laser2, value_laser3
#	print(type(msg))
        parsedMsg = json.loads(str(msg.payload.decode("utf-8","ignore")))
#        print(parsedMsg)
#	print(type(parsedMsg))
#	print(parsedMsg.keys())
        sensorName = str(parsedMsg.keys())
#	print(sensorName[3:10])
        value = 0

        if sensorName.startswith("Sensor0",3,10):
            value = parsedMsg["Sensor0"] / 1020
            mqttClient.publish("lasers/linear/laser0", value)
            print(value)

        elif sensorName.startswith("Sensor1",3,10):
            value = parsedMsg["Sensor1"]
            mqttClient.publish("lasers/linear/laser1", parsedMsg)

        elif sensorName.startswith("Sensor2",3,10):
            value = parsedMsg["Sensor2"]
            mqttClient.publish("lasers/linear/laser2", parsedMsg)

        elif sensorName.startswith("Sensor3",3,10):
            value = parsedMsg["Sensor3"]
            mqttClient.publish("lasers/linear/laser3", parsedMsg)

        else:
            mqttClient.publish("errors", value)
            print(value)

#        print(value)

mqttClient = mqtt.Client()
mqttClient.on_connect = on_connect
mqttClient.on_message = on_message
mqttClient.connect("localhost", 1883, 60)
mqttClient.loop_forever()