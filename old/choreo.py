import paho.mqtt.client as mqtt
import serial
import time
import OSC
import argparse
import json

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("track")
#	client.subscribe("lasers")


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

def binary(data, grenzwert):
    if data > grenzwert:
	retVal = 1
    else:
        retVal = 0
    return retVal

def harfe(data):
    retVal = 1.0
    return retVal

#client = OSC.OSCClient()

#if args.localhost:
#	hostname = args.localhost + ".local"
#	client.connect((args.localhost, 9999))
#elif args.port:
#	client.connect(("192.168.2.3", args.port))
#elif args.port and args.localhost:
#	hostname = args.localhost + ".local"
#	client.connect((args.localhost, args.port))
#else:
#	client.connect(("192.168.178.48", 9999))

ser.flushInput()
try:
	while True:
	        response = ser.readline()
                bundle = OSC.OSCBundle()
		oscmsg = OSC.OSCMessage()
		i = 0
                for word in response.split():
#                   zahl = float(word)
#		    print(zahl)
#
# Je nach Sensor kann funktion ausgewaehlt werden
# linear: Werte zwischen 0.0 und 1.0 die linear dargestellt werden
# binary: ab einem bestimmten wert 0 oder 1
# harfe: der Bereich wird in 0.1 0.2 0.3 ... 1.0 Schritte unterteilt
#  
		    if i == 0:
#			zahl = round(float(word) / 1023,2)
			zahl = binary(float(word), 0.1)
#			zahl = harfe(float(word))
		    elif i == 1:
#			zahl = round(float(word) / 1023,2)
			zahl = binary(float(word), 0.1)
#			zahl = harfe(float(word))
		    elif i == 2:
#			zahl = round(float(word) / 1023,2)
			zahl = binary(float(word), 0.1)
#			zahl = harfe(float(word))
		    elif i == 3:
#			zahl = round(float(word) / 1023,2)
			zahl = binary(float(word), 0.1)
#			zahl = harfe(float(word))
		    else:
			print("i ist nicht das was es soll")

		    oscmsg = OSC.OSCMessage()
		    oscmsg.setAddress('{"/Sensor%d"}' % (i))
                    oscmsg.append(zahl)
                    bundle.append(oscmsg)
                    i += 1

#
# Das lesen von mqtt fuer die tracker werte
#
		def on_message(client, userdata, msg):
		
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
#		client.send(bundle)


except KeyboardInterrupt:
    ser.close()