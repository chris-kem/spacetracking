import subprocess
import keyboard  # using module keyboard

p1 = subprocess.call(['python', 'sensor/seriell-mqtt.py'])
p2 = subprocess.call(['python', 'mqtt-linear.py'])
p3 = subprocess.call(['python', 'mqtt-binary.py'])

#p1.terminate()
#p2.terminate()
#p3.terminate()


while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            p1.exit()
            p2.exit()
            p3.exit()
            break  # finishing the loop
        else:
            pass
    except:
        break  # if user pressed a key other than the given key the loop will break