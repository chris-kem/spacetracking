from subprocess import *

#Popen('python sensor/seriell-mqtt.py')
subprocess.run('python mqtt-linear.py')
subprocess.run('python mqtt-binary.py')
