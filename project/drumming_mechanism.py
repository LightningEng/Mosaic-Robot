#!/usr/bin/env python3

"""
Module to play sounds when ultrasonic sensor detects object within hot-encoded ranges.
This file must be run on the robot.
"""

from utils.brick import TouchSensor, Motor, wait_ready_sensors, reset_brick
from time import delay



DELAY_SEC = 0.01  # seconds of delay between measurements


print("Program start.\nWaiting for sensors to turn on...")

TOUCH_SENSOR = TouchSensor(1)
MOTOR = Motor("A")

INITIAL_POSITION = 0
TARGET_POSITION = 30
MOTOR_POWER = 100

wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.
print("Done waiting.")


def drum():

    #This sets the initial position to 0 degrees ( both arms are touching)
    MOTOR.set_position(INITIAL_POSITION)
    delay(DELAY_SEC)
    #Rotate robot arm to the target position
    MOTOR.set_position(TARGET_POSITION)
    delay(DELAY_SEC)
    


def drummingMechanism():

     # Flag to indicate if drums are active or not active
    drumming= False

    #Initialize Motor Defaults
    MOTOR.set_position_relative(INITIAL_POSITION)
    MOTOR.set_power(MOTOR_POWER)


    try:
        
        while True:
            #sets the drumming tag to its opposite boolean value (makes the touch sensor act as a toggle switch)
            if TOUCH_SENSOR.is_pressed():
                drumming = not drumming
            #makes the robot drum once
            if drumming == True:
                drum()


    except BaseException:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
        pass
    finally:
        print("DDM Deactivated")
        reset_brick() # Turn off everything on the brick's hardware, and reset it
        exit()

if __name__ == "__main__":
    drummingMechanism()