#!/usr/bin/env python3

"""
<<<<<<< Updated upstream
Module to move the slider sunsystem that pushes the cube
=======
Module to play sounds when ultrasonic sensor detects object within hot-encoded ranges.
>>>>>>> Stashed changes
This file must be run on the robot.
"""

from utils.brick import TouchSensor, Motor, wait_ready_sensors, reset_brick
from time import sleep

from math import pi

<<<<<<< Updated upstream
DELAY_SEC = 0.5  # seconds of delay between measurements
=======
DELAY_SEC = 5  # seconds of delay between measurements
>>>>>>> Stashed changes


print("Program start.\nWaiting for sensors to turn on...")

LEFT_WHEEL = Motor("A") #Left Wheel
RIGHT_WHEEL = Motor("B") #Right Wheel 

INITIAL_POSITION = 0
MOTOR_POWER = 100  #power percentage

RADIUS_LEFT_WHEEL = 0.02 #Radius of the left wheel in meters
<<<<<<< Updated upstream
DIST_TO_DEGS_LEFT_WHEEL = 180/(pi*RADIUS_LEFT_WHEEL) #Conversion unit for left wheel to degrees

RADIUS_RIGHT_WHEEL = 0.02 #Radius of the right wheel in meters
DIST_TO_DEGS_RIGHT_WHEEL = 180/(pi*RADIUS_RIGHT_WHEEL) #Conversion unit for right wheel to degrees
=======
DIST_TO_DEGS_LEFT_WHEEL = 180/(3.1416*RADIUS_LEFT_WHEEL) #Conversion unit for left wheel to degrees

RADIUS_RIGHT_WHEEL = 0.02 #Radius of the right wheel in meters
DIST_TO_DEGS_RIGHT_WHEEL = 180/(3.1416*RADIUS_RIGHT_WHEEL) #Conversion unit for right wheel to degrees
>>>>>>> Stashed changes

wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.
print("Done waiting.")

TOUCH_SENSOR = TouchSensor(3)


def move(distance, direction):

<<<<<<< Updated upstream
=======
    #This sets the initial position to 0 degrees ( both arms are touching)
  #  LEFT_WHEEL.set_position(INITIAL_POSITION)
  #  RIGHT_WHEEL.set_position(INITIAL_POSITION)
    
>>>>>>> Stashed changes
    #Set Power and Speed Limits of the Wheels
    LEFT_WHEEL.set_limits(MOTOR_POWER)
    RIGHT_WHEEL.set_limits(MOTOR_POWER)
    
    #Move the wheels with respect to distance and direction
<<<<<<< Updated upstream
    if (direction == 1): #Move Forward
        LEFT_WHEEL.set_position_relative(int(-1*distance*DIST_TO_DEGS_LEFT_WHEEL))
        RIGHT_WHEEL.set_position_relative(int(-1*distance*DIST_TO_DEGS_RIGHT_WHEEL))
    else : #Move Backward
=======
    
    if (direction == 1): #Move Forward
        LEFT_WHEEL.set_position_relative(int(-1*distance*DIST_TO_DEGS_LEFT_WHEEL))
        RIGHT_WHEEL.set_position_relative(int(-1*distance*DIST_TO_DEGS_RIGHT_WHEEL))
    else : #Move
>>>>>>> Stashed changes
        LEFT_WHEEL.set_position_relative(int(distance*DIST_TO_DEGS_LEFT_WHEEL))
        RIGHT_WHEEL.set_position_relative(int(distance*DIST_TO_DEGS_RIGHT_WHEEL))
    
    #rest the engine
    sleep(DELAY_SEC)
    #power down the wheel engines
    LEFT_WHEEL.set_limits(0)
    RIGHT_WHEEL.set_limits(0)
    #rest the engine
    sleep(DELAY_SEC)


def push_pull_Mechanism():

    try:
<<<<<<< Updated upstream
        #Test the move - forward and backward with the same distance
        move(0.2,1)
        move(0.2,0)
=======
        #Initialize Motor Defaults
        
        LEFT_WHEEL.reset_encoder()
        RIGHT_WHEEL.reset_encoder()
        
        LEFT_WHEEL.set_limits(MOTOR_POWER)
        RIGHT_WHEEL.set_limits(MOTOR_POWER)
        
        LEFT_WHEEL.set_position(0)
        RIGHT_WHEEL.set_position(0)
        
        sleep(DELAY_SEC)
        
        LEFT_WHEEL.set_position(-115)
        RIGHT_WHEEL.set_position(-115)
        
        sleep(DELAY_SEC)
        
        LEFT_WHEEL.set_position(-230)
        RIGHT_WHEEL.set_position(-230)
        
        sleep(DELAY_SEC)
        
        LEFT_WHEEL.set_position(-345)
        RIGHT_WHEEL.set_position(-345)
        
        sleep(DELAY_SEC)
        
        LEFT_WHEEL.set_position(-460)
        RIGHT_WHEEL.set_position(-460)
        
        sleep(DELAY_SEC)
        
        LEFT_WHEEL.set_position(0)
        RIGHT_WHEEL.set_position(0)
        
        sleep(DELAY_SEC)
        
        
>>>>>>> Stashed changes

    except BaseException:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
        pass
    finally:
        reset_brick() # Turn off everything on the brick's hardware, and reset it
        exit()

if __name__ == "__main__":
    push_pull_Mechanism()


























































































<<<<<<< Updated upstream
=======



























>>>>>>> Stashed changes
