import serial
import time
import OSC
import argparse
# argparse Funktion um IP-Adresse und Port
# beim starten manuell eingeben zu koennen
parser = argparse.ArgumentParser()
parser.add_argument("-l","--localhost", help="write the hostname of the used computer")
parser.add_argument("-p","--port", type=int, help="which port to send OSC Data")
parser.add_argument("-s","--sensor", type=int, help="which sensor to send only")
args = parser.parse_args()
#ser = serial.Serial("/dev/ttyACM0", 9600)
time.sleep(5)
#ser.write("start reading")
client = OSC.OSCClient()
# Falls beim Starten argparse nicht genutzt wird, Standardwerte verwenden
if args.localhost:
    hostname = args.localhost + ".local"
    client.connect((args.localhost, 9999))
elif args.port:
    client.connect(("192.168.2.3", args.port))
elif args.port and args.localhost:
    hostname = args.localhost + ".local"
    client.connect((args.localhost, args.port))
else:
    client.connect(("192.168.178.48", 9999))
    
try:
    while True:
        response = "500" #ser.readline()
        oscmsg = OSC.OSCMessage()
        # Empfangene Daten in einzelne Sensorwerte aufteilen
        for word in response.split():
            sensorwert = float(word)
            oscmsg.setAddress("/laser0")
            # alle Werte an Message anhaengen
            oscmsg.append(sensorwert)
        print(oscmsg)
    client.send(oscmsg)
except KeyboardInterrupt:
    ser.close()
