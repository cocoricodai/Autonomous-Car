#!/usr/bin/python
import RPi.GPIO as GPIO
import sys
sys.path.append('/home/pi/Sunfounder/config')
import PCA9685 as p
import Config 
import time

class Motor: 
    def __init__(self):
        self.pwm = p.PWM()
        self.pwm.frequency = 60
        GPIO.setwarnings(False) # Disable the warning 
        GPIO.setmode(GPIO.BCM) # We referred to the documentation

        configPins = Config.Config()
        self.M1_Pins = configPins.getPins("Motor-1")

        ### Define pin motor 1 ###
        self.M1_En = int(self.M1_Pins[0]) # En for Enable, means that if it's low, it doesn't work
        self.M1_1A = int(self.M1_Pins[1]) # For The first input (HIGHT)
        self.M1_1B = int(self.M1_Pins[2]) # For The second input (LOW)

        self.M2_Pins = configPins.getPins("Motor-2")
        ### Define pin motor 2 ###
        self.M2_En = int(self.M2_Pins[0]) # En for Enable, means that if it's low, it doesn't work
        self.M2_1A = int(self.M2_Pins[1]) # For The first input (HIGHT)
        self.M2_1B = int(self.M2_Pins[2]) # For The first input (LOW)

        # Set all pins mode as OUT
        self.pins = [self.M1_1A, self.M1_1B,self.M2_1A, self.M2_1B]

    def setup(self):
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)

    # Set de speed of Vehicle
    def setSpeed(self,speed): 
        self.speed = speed
        # Condition to have no problem with sensor
        if speed > 50:
            speed = 50

        elif speed < 0:
            speed = 0

        speed *= 40
        self.pwm.write(self.M1_En, 0, speed)
        self.pwm.write(self.M2_En, 0, speed)

    # Move the Vehicle Forward
    def moveForward(self, speed = 25):
        self.setSpeed(speed) # Set a speed, default = 25
        self.setup()
        
        # Turn ON motors to move forward
        # Motor 1
        GPIO.output(self.M1_1A, GPIO.HIGH)
        GPIO.output(self.M1_1B, GPIO.LOW)

        # Motor 2
        GPIO.output(self.M2_1A, GPIO.HIGH)
        GPIO.output(self.M2_1B, GPIO.LOW)

    # move the Vehicle Backward
    def moveBackward(self, speed = 25):
        self.setSpeed(speed) # Set a speed, default = 25
        self.setup()

        # Turn ON motors to move backward
        # Motor 1
        GPIO.output(self.M1_1A, GPIO.LOW)
        GPIO.output(self.M1_1B, GPIO.HIGH)

        # Motor 2
        GPIO.output(self.M2_1A, GPIO.LOW)
        GPIO.output(self.M2_1B, GPIO.HIGH)
    
    # When the Vehicle has finished all the laps, turn off motors
    def stopMove(self): 
        for pin in self.pins:
            GPIO.output(pin, GPIO.LOW)