#!/usr/bin/python
import RPi.GPIO as GPIO
import sys
sys.path.append('/home/pi/Sunfounder/config')
import Config
from time import sleep

class InfraredSensor:
    def __init__(self, laps):
        GPIO.setmode(GPIO.BCM) # We referred to the documentation
        self.laps = laps # Number of laps the car must do

        configPins = Config.Config()
        self.pinInfraredSensor  = int(configPins.getPins("InfraredSensor")[0])
        
        GPIO.setup(self.pinInfraredSensor, GPIO.IN) # It's a sensor, so, we control the input  
  
    def setup(self):
        GPIO.setup(self.pinInfraredSensor, GPIO.IN) # It's a sensor, so, we control the input


    def isOn(self): 
        self.setup()
        if GPIO.input(self.pinInfraredSensor):# If the sensor finds the line
            self.laps = self.laps -1 # we decrement the laps
            sleep(0.2) # Sleep to not decrement if the speed is low

    def getLaps(self):
        return self.laps # Return laps, when laps = 0, the car stop

