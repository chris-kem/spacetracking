import subprocess
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--localhost", help="write the hostname of the used computer")
parser.add_argument("-p", "--port", type=int, help="which port to send OSC Data")
args = parser.parse_args()

if args.localhost:
    hostname = args.localhost + ".local"
    osc_client.connect((args.localhost, 9999))
elif args.port:
    osc_client.connect(("192.168.2.3", args.port))
elif args.port and args.localhost:
    hostname = args.localhost + ".local"
    osc_client.connect((args.localhost, args.port))
else:
    osc_client.connect(("192.168.178.21", 9999))

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
