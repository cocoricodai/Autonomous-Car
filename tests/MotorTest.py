#!/usr/bin/python
import sys
sys.path.append('/home/pi/Sunfounder')
import time
import Motor


try:
    moteur = Motor.Motor()
    while True:    
        speed = input("Set speed value (0 - 50):")
        moteur.moveForward(int(speed))
        time.sleep(5)
        moteur.moveBackward(int(speed))
        time.sleep(5) 
        
        moteur.stopMove()
finally:
    exit
