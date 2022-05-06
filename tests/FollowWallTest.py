#!/usr/bin/python
import sys
sys.path.append('/home/pi/Sunfounder')
import Vehicle
import time

try:
    principal = Vehicle.Vehicle()
    principal.race(3)

finally:
    exit
