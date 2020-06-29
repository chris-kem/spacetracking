import subprocess
from pynput.keyboard import Key

p1 = subprocess.Popen('python sensor/seriell-mqtt.py')
p2 = subprocess.Popen('python mqtt-linear.py')
p3 = subprocess.Popen('python mqtt-binary.py')

p1.terminate()
p2.terminate()
p3.terminate()

def on_press(key):
    print('{0} pressed'.format(key))
    if key == '\x1b'
        p1.exit()
        p2.exit()
        p3.exit()