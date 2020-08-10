import winsound
import paho.mqtt.client as mqtt
import json
import time

frequency = 32767  # Set Frequency To 2500 Hertz 32767
duration = 100  # Set Duration To 1000 ms == 1 second
print("läuft")


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    mqttClient.subscribe("track")


def on_message(client, userdata, msg):
    converted_msg = float(msg.payload.decode("utf-8", "ignore"))
    value = int(frequency * converted_msg)
    print(value)
    winsound.Beep(value, duration)


mqttClient = mqtt.Client()
mqttClient.on_connect = on_connect
mqttClient.on_message = on_message
mqttClient.connect("localhost", 1883, 60)
mqttClient.loop_forever()
