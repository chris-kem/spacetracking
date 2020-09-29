import subprocess
import time

p1 = subprocess.Popen(
    ["python", "seriell-mqtt.py"], stderr=subprocess.PIPE, stdout=subprocess.PIPE
)
time.sleep(1)
p2 = subprocess.Popen(
    ["python", "mqtt-linear.py"], stderr=subprocess.PIPE, stdout=subprocess.PIPE
)
time.sleep(1)
p3 = subprocess.Popen(
    ["python", "mqtt-OSC.py"], stderr=subprocess.PIPE, stdout=subprocess.PIPE
)
time.sleep(1)
p4 = subprocess.Popen(
    ["python", "track-OSC.py"], stderr=subprocess.PIPE, stdout=subprocess.PIPE
)
time.sleep(1)

try:
    while True:
        print("running")
        time.sleep(10)
except KeyboardInterrupt:
    p1.terminate()
    p2.terminate()
    p3.terminate()
    p4.terminate()
