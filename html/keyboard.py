from pynput.keyboard import Key, Controller
import paho.mqtt.client as mqtt
import json

keyboard = Controller()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("track")


def on_message(client, userdata, msg):
    parsedMsg = json.loads(msg.payload)
    if parsedMsg["value"] == 0.1:
        keyboard.press(Key.f1)
        keyboard.release(Key.f1)
    elif parsedMsg["value"] == 0.2:
        keyboard.press(Key.f2)
        keyboard.release(Key.f2)
    elif parsedMsg["value"] == 0.3:
        keyboard.press(Key.f3)
        keyboard.release(Key.f3)
    elif parsedMsg["value"] == 0.4:
        keyboard.press(Key.f4)
        keyboard.release(Key.f4)
    elif parsedMsg["value"] == 0.5:
        keyboard.press(Key.f5)
        keyboard.release(Key.f5)
    else:
        print("kein feld")


mqttClient = mqtt.Client()
mqttClient.on_connect = on_connect
mqttClient.on_message = on_message
mqttClient.connect("localhost", 1883, 60)
mqttClient.loop_forever()
