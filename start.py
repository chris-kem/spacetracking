import subprocess
import time

p1 = subprocess.Popen('sensor/seriell-mqtt.py')
time.sleep(1)
p2 = subprocess.Popen('mqtt-linear.py')
time.sleep(1)
p3 = subprocess.Popen('mqtt-binary.py')
time.sleep(1)

try:
    while true:
        print(running)
        time.sleep(10)
except: KeyboardInterrupt:
    p3.terminate()
    p2.terminate()
    p1.terminate()