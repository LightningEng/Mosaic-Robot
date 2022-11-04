#!/usr/bin/env python3

"""
Module to play sounds when ultrasonic sensor detects object within hot-encoded ranges.
This file must be run on the robot.
"""

from utils.brick import TouchSensor, Motor, wait_ready_sensors, reset_brick
from time import sleep

from math import pi

DELAY_SEC = 0.01  # seconds of delay between measurements


print("Program start.\nWaiting for sensors to turn on...")

LEFT_WHEEL = Motor("A") #Left Wheel
RIGHT_WHEEL = Motor("B") #Right Wheel 

INITIAL_POSITION = 0
MOTOR_POWER = 100  #power percentage
#MOTOR_SPEED = 720  # degrees/s

RADIUS_LEFT_WHEEL = 0.02 #Radius of the left wheel in meters
DIST_TO_DEGS_LEFT_WHEEL = 180/(3.1416*RADIUS_LEFT_WHEEL) #Conversion unit for left wheel to degrees

RADIUS_RIGHT_WHEEL = 0.02 #Radius of the right wheel in meters
DIST_TO_DEGS_RIGHT_WHEEL = 180/(3.1416*RADIUS_RIGHT_WHEEL) #Conversion unit for right wheel to degrees

wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.
print("Done waiting.")


def move(distance, direction):

    #This sets the initial position to 0 degrees ( both arms are touching)
  #  LEFT_WHEEL.set_position(INITIAL_POSITION)
  #  RIGHT_WHEEL.set_position(INITIAL_POSITION)
    
    #Set Power and Speed Limits of the Wheels
  #  LEFT_WHEEL.set_limits(MOTOR_POWER)
  #  RIGHT_WHEEL.set_limits(MOTOR_POWER)
    
    #Move the wheels with respect to distance and direction
    if (direction == 1):
        LEFT_WHEEL.set_position_relative(int(-1*distance*DIST_TO_DEGS_LEFT_WHEEL))
        RIGHT_WHEEL.set_position_relative(int(-1*distance*DIST_TO_DEGS_RIGHT_WHEEL))
    else :
        LEFT_WHEEL.set_position_relative(int(distance*DIST_TO_DEGS_LEFT_WHEEL))
        RIGHT_WHEEL.set_position_relative(int(distance*DIST_TO_DEGS_RIGHT_WHEEL))
    
    #rest the engine
    sleep(DELAY_SEC)
    #power down the wheel engines
    LEFT_WHEEL.set_limits(0)
    RIGHT_WHEEL.set_limits(0)
    #rest the engine
    sleep(DELAY_SEC)


def pushMechanism():

    try:
        #Initialize Motor Defaults
        move(720,1)

    except BaseException:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
        print("WTF")
        pass
    finally:
        reset_brick() # Turn off everything on the brick's hardware, and reset it
        exit()

if __name__ == "__main__":
    pushMechanism()
