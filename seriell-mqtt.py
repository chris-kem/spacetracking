import paho.mqtt.client as mqtt
import serial
import time
import OSC
import argparse
import json

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("lasers")


cnt_sensor = 4
TRESH = 50
count_laser1 = 0
count_laser0 = 0
value_laser1 = 0
value_laser0 = 0
value = 0

parser = argparse.ArgumentParser()
parser.add_argument("-l","--localhost", help="write the hostname of the used computer")
parser.add_argument("-p","--port", type=int, help="which port to send OSC Data")
parser.add_argument("-s","--sensor", type=int, help="which sensor to send only")
args = parser.parse_args()

ser = serial.Serial("/dev/ttyACM0", 9600)
time.sleep(5)
ser.write("start reading")


ser.flushInput()
try:
    while True:
        response = ser.readline()
        i = 0
        for word in response.split():
            zahl[i] = float(word)
            print(zahl)
            message_out = {"/Sensor%d" % (i) : "zahl[i]"}
            parsedMsg = json.loads(msg.payload)
            oscMessage = OSC.OSCMessage()
            oscMessage.setAddress("/" + parsedMsg["elemid"])
            address = parsedMsg["elemid"]

            value = parsedMsg["value"]
    
            oscMessage.append(float(value))
            bundle.append(oscMessage)

            mqttClient = mqtt.Client()
            mqttClient.on_connect = on_connect
            mqttClient.on_message = on_message
            mqttClient.connect("localhost", 1883, 60)
            mqttClient.loop_forever()
            
            print(bundle)
#       client.send(bundle)


except KeyboardInterrupt:
    ser.close()