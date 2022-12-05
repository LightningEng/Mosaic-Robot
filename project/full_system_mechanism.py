#!/usr/bin/env python3

"""
Module to run the algorithm for the the robot.
"""

from utils.brick import TouchSensor, Motor, wait_ready_sensors, reset_brick
from time import sleep

import input_process_mechanism as inputsGetter

from math import pi

DELAY_SEC = 2.0

#x values starting left to right
x_values = [0,-105, -220, -350, -470]
y_values = [-720, -600,-480,-360,-240]

print("Program start.\nWaiting for sensors to turn on...")

LEFT_WHEEL = Motor("C") #Left Wheel
RIGHT_WHEEL = Motor("B") #Right Wheel
TANK_WHEEL = Motor("A") #Wheel

INITIAL_POSITION = 0
MOTOR_POWER = 100  #power percentage

wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.
print("Done waiting.")





def main():

    try:   
        #Initialize Motor Defaults
        
        LEFT_WHEEL.reset_encoder()
        RIGHT_WHEEL.reset_encoder()
        
        LEFT_WHEEL.set_limits(MOTOR_POWER)
        RIGHT_WHEEL.set_limits(MOTOR_POWER)
               
        TANK_WHEEL.set_limits(MOTOR_POWER)
        
        
        #Input Methods. Choose the one you want and uncomment it. The rest, comment them
        
        #inputArray = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]#[1,0,0,0,0, 0,1,0,0,0, 0,0,1,0,0, 0,0,0,1,0, 0,0,0,0,1]#[0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1]
        
        #Get Input from User
        while True:
            promptInput = input("Keyboard (k)/ Touch sensors (t):")
            if promptInput.lower() == "k":
                inputArray = inputsGetter.getInputByKeyboard()
                break
            if promptInput.lower() == "t":
                inputArray = inputsGetter.getInputByTouchSensors()
                break
            print("Invalid Input")
        
        print(inputArray)
        
        
        #Process input
        modInputArray = []
        modInputArray.append([])
        modInputArray.append([])
        modInputArray.append([])
        modInputArray.append([])
        modInputArray.append([])
        
        k = 0
        for unit in inputArray:
            modInputArray[k].append(unit)
            k = k + 1
            k = k%5                    

        for array in modInputArray:
            array.reverse()
                        
            
        for column in range(len(modInputArray)):
            
            current_sum = sum(modInputArray[column])
            
            if (current_sum == 0): continue
            
            LEFT_WHEEL.set_position(x_values[column]) #move arm to that row
            RIGHT_WHEEL.set_position(x_values[column])
            sleep(DELAY_SEC)            
            
            TANK_WHEEL.set_position_relative(150) #retract claw to drop cube
            sleep(DELAY_SEC)
            
            for row in range(len(modInputArray[column])):
                if (modInputArray[column][row] == 1):    
                    TANK_WHEEL.set_position_relative(y_values[row]) #place cube is proper column
                    sleep(DELAY_SEC)
                    
                    current_sum = current_sum - 1
                    if (current_sum == 0):
                        value = (-1*(y_values[row]))-110
                        TANK_WHEEL.set_position_relative(value) #if current position is in final 1 in row , retract arm back but block next cube from dropping
                        sleep(DELAY_SEC)
                    else:
                        TANK_WHEEL.set_position_relative((-1*y_values[row])+20) #retract arm all the way and next cube drops into claw
                        sleep(DELAY_SEC)
                                
        LEFT_WHEEL.set_position(0) #move arm to that row
        RIGHT_WHEEL.set_position(0)
        sleep(DELAY_SEC)
            
    except BaseException:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
        pass
    finally:
        reset_brick() # Turn off everything on the brick's hardware, and reset it
        exit()

if __name__ == "__main__":
    main()


