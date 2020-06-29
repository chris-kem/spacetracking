import subprocess
import keyboard  # using module keyboard

p1 = subprocess.Popen('sensor/seriell-mqtt.py')
p2 = subprocess.Popen('mqtt-linear.py')
p3 = subprocess.Popen('mqtt-binary.py')


while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            p1.Popen.kill()
            p2.Popen.kill()
            p3.Popen.kill()
            break  # finishing the loop
        else:
            pass
    except:
        break  # if user pressed a key other than the given key the loop will break