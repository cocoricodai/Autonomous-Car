#!/usr/bin/python
import sys
sys.path.append('/home/pi/Sunfounder')
import time
import UltrasoundSensor


try:
    sensorL = UltrasoundSensor.UltrasoundSensor("left")
    sensorR = UltrasoundSensor.UltrasoundSensor("right")
    sensorF = UltrasoundSensor.UltrasoundSensor("front")

    isOK = True
    while isOK:    
        print("L : " , sensorL.getDistance())
        print("F : " , sensorF.getDistance())
        print("R : " , sensorR.getDistance())
        continu = input("Stop programm (y/n)? : ")
        if continu == "y" :
            isOK = False
        
finally:
    exit
