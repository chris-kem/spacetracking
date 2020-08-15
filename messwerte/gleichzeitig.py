import subprocess
import time

p1 = subprocess.Popen(
    ["python", "deca_messen.py"], stderr=subprocess.PIPE, stdout=subprocess.PIPE
)
time.sleep(1)
p2 = subprocess.Popen(
    ["python", "htc_messen.py"], stderr=subprocess.PIPE, stdout=subprocess.PIPE
)
time.sleep(1)

try:
    while True:
        print("running")
        time.sleep(10)
except KeyboardInterrupt:
    p1.terminate()
    p2.terminate()
