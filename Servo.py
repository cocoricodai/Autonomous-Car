#!/usr/bin/python
import RPi.GPIO as GPIO
import sys
sys.path.append('/home/pi/Sunfounder/config')
from adafruit_servokit import ServoKit
import Config 
import time

class Servo:
    def __init__(self):
        configPins = Config.Config()
        self.channel = int(configPins.getPins("Servo")[0])
        self.kit = ServoKit(channels=8)
        self.angleMax = 95
        self.angleMin = 45
        self.angleMid = 70

    # Sets the angle ourself
    def setAngle(self, angle):
        # Condition to have no problem with sensor
        if angle < self.angleMin :
            angle = self.angleMin

        elif angle > self.angleMax :
            angle = self.angleMax

        self.kit.servo[self.channel].actuation_range = self.angleMax
        self.kit.servo[self.channel].angle = angle

    # Define the good angle with distance
    def setAngleByDist(self, distance):
        angle = (distance/20) * self.angleMid # Equation in order to have the right angle
        self.kit.servo[self.channel].actuation_range = self.angleMax

        # Condition to have no problem with sensor
        if angle < self.angleMin :
            angle = self.angleMin

        elif angle > self.angleMax :
            angle = self.angleMax

        if distance > 21 and distance < 23:
            self.kit.servo[self.channel].angle = self.angleMid + 10

        if distance != 22 :
            self.kit.servo[self.channel].angle = angle
        
        