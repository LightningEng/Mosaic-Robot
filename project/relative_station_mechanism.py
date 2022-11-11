#!/usr/bin/env python3

"""
Module to push the cube using the slider
This file must be run on the robot.
"""

from utils.brick import TouchSensor, Motor, wait_ready_sensors, reset_brick
from time import sleep

from math import pi

DELAY_SEC = 2  # seconds of delay between measurements

print("Program start.\nWaiting for sensors to turn on...")


MOTOR_POWER = 100  #power percentage

TANK_WHEEL = Motor("C") #Wheel

RADIUS_TANK_WHEEL = 0.02 #Radius of the left wheel in meters
DIST_TO_DEGS_TANK_WHEEL = 180/(pi*RADIUS_TANK_WHEEL) #Conversion unit for left wheel to degrees



wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.
print("Done waiting.")



def wheelMove(distance, direction):
    #Set Power and Speed Limits of the Wheels
    TANK_WHEEL.set_limits(MOTOR_POWER)
    
    #Move the wheels with respect to distance and direction
    if (direction == 1): #Move Forward
        TANK_WHEEL.set_position_relative(int(-1*distance*DIST_TO_DEGS_TANK_WHEEL))
    else : #Move Backward
        TANK_WHEEL.set_position_relative(int(distance*DIST_TO_DEGS_TANK_WHEEL))
    
    #rest the engine
    sleep(DELAY_SEC)

    

def tankMechanism():
    
    try:
        #Test the move - forward and backward with the same distance
        wheelMove(0.20,1)
        wheelMove(0.20,0)
        
    except BaseException:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
        pass
    finally:
        reset_brick() # Turn off everything on the brick's hardware, and reset it
        exit()

if __name__ == "__main__":
    tankMechanism()