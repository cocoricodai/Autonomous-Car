#!/usr/bin/python
import sys
sys.path.append('/home/pi/Sunfounder')
import InfraredSensor
import time 

try:
    laps = input("Choose number of laps : ")
    sensor = InfraredSensor.InfraredSensor(int(laps))
    while(sensor.getLaps() > 0):
        sensor.isOn()
        print("Le tour : " , sensor.getLaps())
        
finally:
    exit
