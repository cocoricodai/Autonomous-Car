#!/usr/bin/python
import sys
sys.path.append('/home/pi/Sunfounder')
import Vehicle
import time

try:
    principal = Vehicle.Vehicle()
    isOK = True
    while isOK:
        angle = input("Set a angle (60 - 120): ")
        speed = input("Set a speed (0 - 50): ")
        principal.circular(int(angle) , int(speed))
        continu = input("Stop programm (y/n)? : ")
        if continu == "y" :
            isOK = False
        
    principal.motor.stopMove()
        
finally:
    exit
