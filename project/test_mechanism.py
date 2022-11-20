#!/usr/bin/env python3

"""
Module to run the algorithm for the the robot.
"""

from utils.brick import TouchSensor, Motor, wait_ready_sensors, reset_brick
from time import sleep

from math import pi

DELAY_SEC = 1.5  # seconds of delay between measurements
                #j
input_array = [ [0,0,0,0,0], #i
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [1,1,1,1,1]]

#x values starting left to right
x_values = [0,-115, -230, -345, -460]
y_values = [-710, -600,-480,-360,-240]

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
        
        for i in range(0,len(input_array)):
            if sum(input_array[i]) > 0:  #if there are any 1 in the currrent row
                LEFT_WHEEL.set_position(x_values[i]) #move arm to that row
                RIGHT_WHEEL.set_position(x_values[i])
                sleep(DELAY_SEC)
                TANK_WHEEL.set_position_relative(110) #retract claw to drop cube
                sleep(DELAY_SEC)
                tmp = input_array[i].copy()
                tmp.reverse()
                get_last = 4 - tmp.index(1) #find positon last 1 in current row
            for j in range(len(input_array[i])): #iterate through the columns
                if input_array[i][j] == 1:
                    TANK_WHEEL.set_position_relative(y_values[j]) #place cube is proper column
                    sleep(DELAY_SEC)
                    if j == get_last:
                        TANK_WHEEL.set_position_relative(-1*(y_values[j])-110) #if current position is in final 1 in row , retract arm back but block next cube from dropping
                        sleep(DELAY_SEC)
                    else:
                        TANK_WHEEL.set_position_relative(-1*y_values[j]+10) #retract arm all the way and next cube drops into claw
            
        LEFT_WHEEL.set_position(0) #move arm to that row
        RIGHT_WHEEL.set_position(0)
        sleep(DELAY_SEC)
    except BaseException:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
        pass
    finally:
        reset_brick() # Turn off everything on the brick's hardware, and reset it
        exit()

if __name__ == "__main__":
    algorithm()






















































































































