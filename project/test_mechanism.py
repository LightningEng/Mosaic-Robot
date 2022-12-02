#!/usr/bin/env python3

"""
Module to run the algorithm for the the robot.
"""

from utils.brick import TouchSensor, Motor, wait_ready_sensors, reset_brick
from time import sleep

from math import pi

DELAY_SEC = 2.0

#x values starting left to right
x_values = [0,-115, -225, -335, -450]
y_values = [-710, -600,-480,-360,-240]

print("Program start.\nWaiting for sensors to turn on...")

LEFT_WHEEL = Motor("A") #Left Wheel
RIGHT_WHEEL = Motor("B") #Right Wheel
TANK_WHEEL = Motor("C") #Wheel

INITIAL_POSITION = 0
MOTOR_POWER = 100  #power percentage

wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.
print("Done waiting.")

def getInputByKeyboard():
    while True:
        
        arr = []
        user_input = ''

        print("Must Enter 25 Numbers! Only 0s and 1s")

        numOnes = 0

        while len(arr) < 25: #get 25 cubes
            #Get input from user
            user_input = input('Enter a number either 0 or 1: ')
            
            if (user_input.isdigit()): #Check if valid data, specifically if it is a digit
                num = int(user_input)
                if num == 0 or num == 1: #if 0 or 1, store it
                    arr.append(num)
                    if num == 1:
                        numOnes += 1 #increment number of 1s
                    
                else:
                    print("Invalid input! Only 0 or 1")
            else:
                print("Invalid input! Only 0 or 1")
                
        if numOnes <= 15: #Check if the number of required cubes do not exceed 15
            if numOnes == 0:
                arr = []
            break
        else:
            numOnes = 0
            arr = []
            print("Too many 1s. Start from scratch!")
    
    return arr

def algorithm():

    try:
        
        #Initialize Motor Defaults
        
        LEFT_WHEEL.reset_encoder()
        RIGHT_WHEEL.reset_encoder()
        
        LEFT_WHEEL.set_limits(MOTOR_POWER)
        RIGHT_WHEEL.set_limits(MOTOR_POWER)
               
        TANK_WHEEL.set_limits(MOTOR_POWER)
        
        #Get input by Input Method 1
        inputArray = getInputByKeyboard()
        
        #Modify input array such that every column is reversed to optimize the performance and to prove correctness
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
                        
        
        #Algorithm for placing the cubes
        for column in range(len(modInputArray)):
            
            current_sum = sum(modInputArray[column])
            
            if (current_sum == 0): continue
            
            LEFT_WHEEL.set_position(x_values[column]) #move arm to that row
            RIGHT_WHEEL.set_position(x_values[column])
            sleep(DELAY_SEC)            
            
            TANK_WHEEL.set_position_relative(150) #retract claw to drop cube
            sleep(DELAY_SEC)
            
            for row in range(len(modInputArray[column])):
                if (modInputArray[column][row] == 1):     #for every cube within that column
                    TANK_WHEEL.set_position_relative(y_values[row]) #place cube to proper row
                    sleep(DELAY_SEC)
                    
                    current_sum = current_sum - 1 #update the number of cubes
                    if (current_sum == 0):
                        value = (-1*(y_values[row]))-110
                        TANK_WHEEL.set_position_relative(value) #if current position is in final 1 in row , retract arm back but block next cube from dropping
                        sleep(DELAY_SEC)
                    else:
                        TANK_WHEEL.set_position_relative((-1*y_values[row])+20) #retract arm all the way and next cube drops into claw
                        sleep(DELAY_SEC)
        
        #move arm to initial position
        LEFT_WHEEL.reset_encoder()
        RIGHT_WHEEL.reset_encoder()
        LEFT_WHEEL.set_position_relative(585) 
        RIGHT_WHEEL.set_position_relative(585)
        sleep(DELAY_SEC)
            
    except BaseException:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
        pass
    finally:
        reset_brick() # Turn off everything on the brick's hardware, and reset it
        exit()

if __name__ == "__main__":
    algorithm()


