"""Small example OSC server

This program listens to several addresses, and prints some information about
received packets.
"""
import argparse
import math
import OSC

from time import sleep

osc = OSC.OSCServer( ("localhost", 9999) )
osc.timeout = 0
run = True

