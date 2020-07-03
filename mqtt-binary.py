import paho.mqtt.client as mqtt
import cgi
import json
import time

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	mqttClient.subscribe("lasers/raw/#")
# test
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
#	print(parsedMsg["Sensor2"])
#	print(parsedMsg.keys())
	key_name = str(parsedMsg.keys())
	sensorName = key_name[3:10]
#	print(sensorName)
        value = 0

        if sensorName.startswith("Sensor0"):
            value = value_laser0
            if float(parsedMsg["Sensor0"]) > .2:
                value = 1
                count_laser0 = 0
            else:
                count_laser0 += 1

                if count_laser0 > TRESH:
                    value = 0

            value_laser0 = value
	    data_out = json.dumps({"Sensor0" : value})
	    mqttClient.publish("lasers/binary/laser0", data_out)

        elif sensorName.startswith("Sensor1"):
            value = value_laser1

            if float(parsedMsg["Sensor1"]) > .3:
                value = 1
                count_laser1 = 0
            else:
                count_laser1 += 1

                if count_laser1 > TRESH:
                    value = 0

            value_laser1 = value
            data_out = json.dumps({"Sensor1" : value})
            mqttClient.publish("lasers/binary/laser1", data_out)


        elif sensorName.startswith("Sensor2"):
            value = value_laser2

            if float(parsedMsg["Sensor2"]) > .3:
                value = 1
                count_laser2 = 0
            else:
                count_laser2 += 1

                if count_laser2 > TRESH:
                    value = 0

            value_laser2 = value
            data_out = json.dumps({"Sensor2" : value})
            mqttClient.publish("lasers/binary/laser2", data_out)

        elif sensorName.startswith("Sensor3"):
            value = value_laser3

            if float(parsedMsg["Sensor3"]) > .3:
                value = 1
                count_laser3 = 0
            else:
                count_laser3 += 1

                if count_laser3 > TRESH:
                    value = 0

            value_laser3 = value
            data_out = json.dumps({"Sensor3" : value})
            mqttClient.publish("lasers/binary/laser3", data_out)


        else:
	    mqttClient.publish("errors", value)
	    print("error %d" + value)

       # print(value)

mqttClient = mqtt.Client()
mqttClient.on_connect = on_connect
mqttClient.on_message = on_message
mqttClient.connect("localhost", 1883, 60)
mqttClient.loop_forever()
