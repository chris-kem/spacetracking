import paho.mqtt.client as mqtt
import serial
import time
import json

# liest die sensorwerte uber die serielle Schnittstelle aus
# und leitet die daten per mqtt weiter


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))


ser = serial.Serial("/dev/ttyACM0", 9600)
time.sleep(5)
ser.write("start reading")

mqttClient = mqtt.Client()
mqttClient.on_connect = on_connect
mqttClient.connect("localhost", 1883, 60)

ser.flushInput()
try:
    while True:
        response = ser.readline()
#	print(response)
        i = 0
        for word in response.split():
            zahl = float(word)
            # print(zahl)
            message_out = {"Sensor%d" % (i): zahl}
            parsedMsg = json.dumps(message_out)
#            print(parsedMsg)
            if i == 0:
                mqttClient.publish("lasers/raw/laser0", parsedMsg)
#		print(parsedMsg)
            elif i == 1:
                mqttClient.publish("lasers/raw/laser1", parsedMsg)
            elif i == 2:
                mqttClient.publish("lasers/raw/laser2", parsedMsg)
            elif i == 3:
                mqttClient.publish("lasers/raw/laser3", parsedMsg)
            else:
                mqttClient.publish("errors", "Fehler bei seriell zu mqtt")

#	    mqttClient.loop_forever()
            i += 1

except KeyboardInterrupt:
    ser.close()
