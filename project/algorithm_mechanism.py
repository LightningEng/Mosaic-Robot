#!/usr/bin/env python3

"""
Module to play sounds when ultrasonic sensor detects object within hot-encoded ranges.
This file must be run on the robot.
"""

from utils.brick import TouchSensor, Motor, wait_ready_sensors, reset_brick
from time import sleep

from math import pi

DELAY_SEC = 1.5  # seconds of delay between measurements


print("Program start.\nWaiting for sensors to turn on...")

LEFT_WHEEL = Motor("A") #Left Wheel
RIGHT_WHEEL = Motor("B") #Right Wheel
TANK_WHEEL = Motor("C") #Wheel

INITIAL_POSITION = 0
MOTOR_POWER = 100  #power percentage

wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.
print("Done waiting.")



def algorithm():

    try:
        #Initialize Motor Defaults
        
        LEFT_WHEEL.reset_encoder()
        RIGHT_WHEEL.reset_encoder()
        
        LEFT_WHEEL.set_limits(MOTOR_POWER)
        RIGHT_WHEEL.set_limits(MOTOR_POWER)
            
        
                
        TANK_WHEEL.set_limits(MOTOR_POWER)
        
        
        
        #Move
        
        LEFT_WHEEL.set_position(0)
        RIGHT_WHEEL.set_position(0)
        sleep(DELAY_SEC)
        TANK_WHEEL.set_position_relative(110)
        sleep(DELAY_SEC)
        TANK_WHEEL.set_position_relative(-710)
        sleep(DELAY_SEC)
        TANK_WHEEL.set_position_relative(600)
        sleep(DELAY_SEC)
        
        
        LEFT_WHEEL.set_position(-115)
        RIGHT_WHEEL.set_position(-115)
        sleep(DELAY_SEC)
        TANK_WHEEL.set_position_relative(110)
        sleep(DELAY_SEC)
        TANK_WHEEL.set_position_relative(-600)
        sleep(DELAY_SEC)
        TANK_WHEEL.set_position_relative(490)
        sleep(DELAY_SEC)
        
        
        LEFT_WHEEL.set_position(-230)
        RIGHT_WHEEL.set_position(-230)
        sleep(DELAY_SEC)
        TANK_WHEEL.set_position_relative(110)
        sleep(DELAY_SEC)
        TANK_WHEEL.set_position_relative(-480)
        sleep(DELAY_SEC)
        TANK_WHEEL.set_position_relative(370)
        sleep(DELAY_SEC)
        
        
        LEFT_WHEEL.set_position(-345)
        RIGHT_WHEEL.set_position(-345)
        sleep(DELAY_SEC)
        TANK_WHEEL.set_position_relative(110)
        sleep(DELAY_SEC)
        TANK_WHEEL.set_position_relative(-360)
        sleep(DELAY_SEC)
        TANK_WHEEL.set_position_relative(250)
        sleep(DELAY_SEC)
        
        
        LEFT_WHEEL.set_position(-460)
        RIGHT_WHEEL.set_position(-460)
        sleep(DELAY_SEC)
        TANK_WHEEL.set_position_relative(110)
        sleep(DELAY_SEC)
        TANK_WHEEL.set_position_relative(-240)
        sleep(DELAY_SEC)
        TANK_WHEEL.set_position_relative(130)
        sleep(DELAY_SEC)
        
        
        LEFT_WHEEL.set_position(0)
        RIGHT_WHEEL.set_position(0)
        sleep(DELAY_SEC)
#         
        
        
        
        
        

    except BaseException:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
        pass
    finally:
        reset_brick() # Turn off everything on the brick's hardware, and reset it
        exit()

if __name__ == "__main__":
    algorithm()






















































































































