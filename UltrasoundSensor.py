#!/usr/bin/python
import RPi.GPIO as GPIO
import sys
sys.path.append('/home/pi/Sunfounder/config')
import Config 
import time

class UltrasoundSensor():
    def __init__(self, position):
        GPIO.cleanup()
        self.position = position

        self.pulse_start = 0
        self.pulse_end = 0
        self.pulse_duration = 0

        configPins = Config.Config()

        if(self.position == "left"): # Set pin LEFT
            self.sensorL = configPins.getPins("UltrasoundSensor-Left")
            self.TRIG = int(self.sensorL[0])
            self.ECHO = int(self.sensorL[1])
        
        elif(self.position == "right"): # Set pin RIGHT
            self.sensorR = configPins.getPins("UltrasoundSensor-Right")
            self.TRIG = int(self.sensorR[0])
            self.ECHO = int(self.sensorR[1])

        elif(self.position == "front"): # Set pin FRONT
            self.sensorF = configPins.getPins("UltrasoundSensor-Front")
            self.TRIG = int(self.sensorF[0])
            self.ECHO = int(self.sensorF[1])

        GPIO.setwarnings(False) # We disabled the warnings
        GPIO.setmode(GPIO.BCM) # We referred to the documentation


    def setup(self):
        GPIO.setup(self.TRIG,GPIO.OUT)
        GPIO.setup(self.ECHO,GPIO.IN)

    def getDistance(self): # Convert time to distance
        self.setup()
        GPIO.output(self.TRIG, False)                 
        time.sleep(0.0001)                            
        GPIO.output(self.TRIG, True)                  
        time.sleep(0.00001)                      
        GPIO.output(self.TRIG, False)  
        while GPIO.input(self.ECHO)==0:                
            self.pulse_start = time.time()  
        while GPIO.input(self.ECHO)==1:              
            self.pulse_end = time.time()                 

        self.pulse_duration = self.pulse_end - self.pulse_start 

        distance = self.pulse_duration * 17150    
        distance = round(distance, 2)      
        if distance > 2:
            return distance - 0.5
        else :
            return 0