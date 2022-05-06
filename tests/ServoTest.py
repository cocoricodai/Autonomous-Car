#!/usr/bin/python
import sys
sys.path.append('/home/pi/Sunfounder')
import time
import Servo

try :
    servo = Servo.Servo()
    isOK = True
    while isOK:
        angle = input("Angle (60 - 120) :")
        servo.setAngle(int(angle))
        continu = input("Stop programm (y/n)? : ")
        if continu == "y" :
            isOK = False
            
finally:
    exit
