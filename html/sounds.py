import winsound
import paho.mqtt.client as mqtt
import json
import time

frequency = 320  # Set Frequency To 2500 Hertz 32767
duration = 5000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    mqttClient.subscribe("track")


def on_message(client, userdata, msg):
    converted_msg = json.loads(str(msg.payload.decode("utf-8", "ignore")))
    value = converted_msg.value()
    print(value)
    winsound.Beep(frequency * value, duration)


mqttClient = mqtt.Client()
mqttClient.on_connect = on_connect
mqttClient.on_message = on_message
mqttClient.connect("localhost", 1883, 60)
mqttClient.loop_forever()
