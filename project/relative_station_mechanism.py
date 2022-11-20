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



def wheelMove(angle, direction):
    
    #Set Power and Speed Limits of the Wheels
    TANK_WHEEL.set_limits(MOTOR_POWER)
    
    #Move the wheels with respect to distance and direction
    if (direction == 1):
        TANK_WHEEL.set_position_relative(int(-1*angle))
    else :
        TANK_WHEEL.set_position_relative(int(angle))
    
    #rest the engine
    sleep(DELAY_SEC)
    #power down the wheel engines
    #TANK_WHEEL.set_limits(0)
    #rest the engine
    #sleep(0.5)
    
    

    

def relative_station_mechanism():
    
    try:
        #Initialize Motor Defaults
        TANK_WHEEL.set_limits(MOTOR_POWER)
        
        #The push-pull stick is set up such that it blocks the cubes from touching the ground.
        TANK_WHEEL.set_position_relative(100) #Retract the system such that the cube is placed on the ground from the cube tower (disposal)
        sleep(DELAY_SEC)
        TANK_WHEEL.set_position_relative(-710) #Push the cube to the last row (5th row) of the grid
        sleep(DELAY_SEC)
        TANK_WHEEL.set_position_relative(720) #Retract the stick to initial position such that it blocks the cubes from touching the ground.
        sleep(DELAY_SEC)
        
        TANK_WHEEL.set_position_relative(-600) #Push the cube to the 4th row of the grid
        sleep(DELAY_SEC)
        TANK_WHEEL.set_position_relative(610) #Retract the stick to initial position such that it blocks the cubes from touching the ground.
        sleep(DELAY_SEC)
        
        TANK_WHEEL.set_position_relative(-480) #Push the cube to the 3rd row of the grid
        sleep(DELAY_SEC)
        TANK_WHEEL.set_position_relative(490) #Retract the stick to initial position such that it blocks the cubes from touching the ground.
        sleep(DELAY_SEC)
        
        TANK_WHEEL.set_position_relative(-360) #Push the cube to the 2nd row of the grid
        sleep(DELAY_SEC)
        TANK_WHEEL.set_position_relative(370) #Retract the stick to initial position such that it blocks the cubes from touching the ground.
        sleep(DELAY_SEC)
        
        TANK_WHEEL.set_position_relative(-240) #Push the cube to the 1rst row of the grid
        sleep(DELAY_SEC)
        TANK_WHEEL.set_position_relative(130) #Retract the stick to initial position such that it blocks the cubes from touching the ground.
        sleep(DELAY_SEC)
        
    except BaseException:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
        pass
    finally:
        reset_brick() # Turn off everything on the brick's hardware, and reset it
        exit()

if __name__ == "__main__":
    relative_station_mechanism()