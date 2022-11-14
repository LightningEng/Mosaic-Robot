#!/usr/bin/env python3

"""
<<<<<<< Updated upstream
Module to push the cube using the slider
=======
Module to play sounds when ultrasonic sensor detects object within hot-encoded ranges.
>>>>>>> Stashed changes
This file must be run on the robot.
"""

from utils.brick import TouchSensor, Motor, wait_ready_sensors, reset_brick
from time import sleep

from math import pi

<<<<<<< Updated upstream
DELAY_SEC = 2  # seconds of delay between measurements
=======
DELAY_SEC = 1.5  # seconds of delay between measurements
>>>>>>> Stashed changes

print("Program start.\nWaiting for sensors to turn on...")


MOTOR_POWER = 100  #power percentage

TANK_WHEEL = Motor("C") #Wheel

RADIUS_TANK_WHEEL = 0.02 #Radius of the left wheel in meters
DIST_TO_DEGS_TANK_WHEEL = 180/(pi*RADIUS_TANK_WHEEL) #Conversion unit for left wheel to degrees



wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.
print("Done waiting.")



<<<<<<< Updated upstream
def wheelMove(distance, direction):
=======
def wheelMove(angle, direction):
    
>>>>>>> Stashed changes
    #Set Power and Speed Limits of the Wheels
    TANK_WHEEL.set_limits(MOTOR_POWER)
    
    #Move the wheels with respect to distance and direction
<<<<<<< Updated upstream
    if (direction == 1): #Move Forward
        TANK_WHEEL.set_position_relative(int(-1*distance*DIST_TO_DEGS_TANK_WHEEL))
    else : #Move Backward
        TANK_WHEEL.set_position_relative(int(distance*DIST_TO_DEGS_TANK_WHEEL))
    
    #rest the engine
    sleep(DELAY_SEC)
=======
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
    
    
>>>>>>> Stashed changes

    

def tankMechanism():
    
    try:
<<<<<<< Updated upstream
        #Test the move - forward and backward with the same distance
        wheelMove(0.20,1)
        wheelMove(0.20,0)
=======
        #Initialize Motor Defaults
        
        #TANK_WHEEL.reset_encoder()
        
        TANK_WHEEL.set_limits(MOTOR_POWER)
        TANK_WHEEL.set_position_relative(100)
        sleep(DELAY_SEC)
        TANK_WHEEL.set_position_relative(-710)
        sleep(DELAY_SEC)
        TANK_WHEEL.set_position_relative(720)
        sleep(DELAY_SEC)
        
        
        TANK_WHEEL.set_position_relative(-600)
        sleep(DELAY_SEC)
        TANK_WHEEL.set_position_relative(610)
        sleep(DELAY_SEC)
        
        TANK_WHEEL.set_position_relative(-480)
        sleep(DELAY_SEC)
        TANK_WHEEL.set_position_relative(490)
        sleep(DELAY_SEC)
        
        
        TANK_WHEEL.set_position_relative(-360)
        sleep(DELAY_SEC)
        TANK_WHEEL.set_position_relative(370)
        sleep(DELAY_SEC)
        
        TANK_WHEEL.set_position_relative(-240)
        sleep(DELAY_SEC)
        TANK_WHEEL.set_position_relative(130)
        sleep(DELAY_SEC)
        
        
        
        
        
>>>>>>> Stashed changes
        
    except BaseException:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
        pass
    finally:
        reset_brick() # Turn off everything on the brick's hardware, and reset it
        exit()

if __name__ == "__main__":
    tankMechanism()