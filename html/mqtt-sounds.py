import paho.mqtt.client as mqtt
import json
import time


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    mqttClient.subscribe("track")


def on_message(client, userdata, msg):
    mqttClient.publish("lasers/linear/laser0", round(value, 2))


mqttClient = mqtt.Client()
mqttClient.on_connect = on_connect
mqttClient.on_message = on_message
mqttClient.connect("localhost", 1883, 60)
mqttClient.loop_forever()
