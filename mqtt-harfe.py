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
#	print(type(parsedMsg))
#	print(parsedMsg.keys())
	    sensorName = str(parsedMsg.keys())
#	print(sensorName[3:10])
        value = 0

        if sensorName.startswith("Sensor0",3,10):
            value = value_laser0
            if float(parsedMsg["Sensor0"]) > .1:
                value = 1
                count_laser0 = 0
            else:
                count_laser0 += 1

                if count_laser0 > TRESH:
                    value = 0

            value_laser0 = value
	    mqttClient.publish("lasers/binary/laser0", value)

        elif sensorName.startswith("Sensor1",3,10):
            value = value_laser1

            if float(parsedMsg["value"]) > .3:
                value = 1
                count_laser1 = 0
            else:
                count_laser1 += 1

                if count_laser1 > TRESH:
                    value = 0

            value_laser1 = value
	    mqttClient.publish("lasers/binary/laser1", value)

        elif sensorName.startswith("Sensor2",3,10):
            value = value_laser2

            if float(parsedMsg["value"]) > .3:
                value = 1
                count_laser2 = 0
            else:
                count_laser2 += 1

                if count_laser2 > TRESH:
                    value = 0

            value_laser2 = value
	    mqttClient.publish("lasers/binary/laser2", value)

        elif sensorName.startswith("Sensor3",3,10):
            value = value_laser3

            if float(parsedMsg["value"]) > .3:
                value = 1
                count_laser3 = 0
            else:
                count_laser3 += 1

                if count_laser3 > TRESH:
                    value = 0

            value_laser3 = value
	    mqttClient.publish("lasers/binary/laser3", value)

        else:
	    mqttClient.publish("errors", value)
	    print(value)

        #print(value)

mqttClient = mqtt.Client()
mqttClient.on_connect = on_connect
mqttClient.on_message = on_message
mqttClient.connect("localhost", 1883, 60)
mqttClient.loop_forever()