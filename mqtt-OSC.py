import paho.mqtt.client as mqtt
import json
import serial
import time
import OSC
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--localhost",
                    help="write the hostname of the used computer")
parser.add_argument("-p", "--port", type=int,
                    help="which port to send OSC Data")
args = parser.parse_args()

osc_client = OSC.OSCClient()

if args.localhost:
    hostname = args.localhost + ".local"
    osc_client.connect((args.localhost, 9999))
elif args.port:
    osc_client.connect(("192.168.2.3", args.port))
elif args.port and args.localhost:
    hostname = args.localhost + ".local"
    osc_client.connect((args.localhost, args.port))
else:
    osc_client.connect(("192.168.178.21", 9999))
# empfängt über mqtt die daten der website und leitet diese per OSC message
# weiter damit diese in musik gewandelt wird


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("lasers/OSC/#")
#    client.subscribe("lasers/raw/#")


def on_message(client, userdata, msg):
    bundle = OSC.OSCBundle()
    oscmsg = OSC.OSCMessage()
#        print(msg)
    parsedMsg = json.loads(msg.payload)
#        print(parsedMsg)
#        print(parsedMsg.values())
    sensorName = str(parsedMsg.keys())
    id = sensorName[9:10]
#	print("test%d" % int(id))
    oscmsg.setAddress('{"/Sensor%d"}' % int(id))
    oscmsg.append(parsedMsg.values())
    print(oscmsg)
    osc_client.send(oscmsg)


mqttClient = mqtt.Client()
mqttClient.on_connect = on_connect
mqttClient.on_message = on_message
mqttClient.connect("localhost", 1883, 60)
mqttClient.loop_forever()
