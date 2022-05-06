import time 
import math
from InfraredSensor import *
from Motor import *
from Servo import *
from UltrasoundSensor import *

class Vehicle:
    def __init__(self):
        # Motor
        self.motor = Motor()

        # Servo 
        self.servo = Servo()

        # UltrasoundSensor
        self.sensorL = UltrasoundSensor("left")
        self.sensorR = UltrasoundSensor("right")
        self.sensorF = UltrasoundSensor("front")

    # Method to show that we know how to make a circle in both direction
    def circular(self, angle, speed):
        self.servo.setAngle(angle)
        self.motor.moveForward(speed)

    # Run along the right wall
    def race(self,laps):
        self.infraredSensor = InfraredSensor(laps)
        self.motor.moveForward(50)
        while self.infraredSensor.getLaps() > 0:
            self.infraredSensor.isOn()
            position_to_wall = self.sensorR.getDistance()
            self.servo.setAngleByDist(position_to_wall)
        self.motor.stopMove()


    # Method to avoid an obstacle
    def obstacleAvoidance(self):
        distance_to_object = self.sensorF.getDistance()
        self.motor.moveForward(40)
        self.servo.setAngle(self.servo.angleMid)
        print(distance_to_object)
        if distance_to_object < 15:
            self.servo.setAngle(self.servo.angleMid)
            self.motor.moveBackward(50)
            time.sleep(1)
        elif distance_to_object < 40:
            self.motor.moveForward(20)
            self.servo.setAngle(self.servo.angleMax)
        else :
            self.servo.setAngle(self.servo.angleMid)
            self.motor.moveForward(40)

        
if __name__ == "__main__":
    vehicle = Vehicle()
    laps = int(input("Enter number of laps : "))
    laps = laps + 1
    position = input("Follow right or left ? : ")
    vehicle.race(laps)
        
 
    
        