#!/usr/bin/python
import sys
sys.path.append('/home/pi/Sunfounder')
import Vehicle
import time

try:
    principal = Vehicle.Vehicle()
    while True:
        principal.obstacleAvoidance()
finally:
    exit
 