#!/usr/bin/env python3

"""
Module to run the main program
This file must be run on the robot.
"""
from utils import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors, reset_brick
from time import sleep

from threading import Thread

print("Program start.\nWaiting for sensors to turn on...")


Input_0_SENSOR = TouchSensor(1)
Input_1_SENSOR = TouchSensor(2)


wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.
print("Done waiting.")


numElements = [0,0] #total number of 0s and 1s, and total number of 1s

arr = []


def getInputByKeyboard():
    while True:
        
        arr = []
        user_input = ''

        print("Must Enter 25 Numbers! Only 0s and 1s! At most 15 1s!")

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
 
def button0Checking():
    global arr
    while numElements[0] < 25:
        if (Input_0_SENSOR.is_pressed()):
            print("0 pressed")
            numElements[0] += 1
            arr.append(0)
            while Input_0_SENSOR.is_pressed():
                sleep(0.01)
        sleep(0.01)
    return
        
def button1Checking():
    global arr
    while numElements[0] < 25:
        if (Input_1_SENSOR.is_pressed()):
            print("1 pressed")
            numElements[0] += 1
            numElements[1] += 1
            arr.append(1)
            while Input_1_SENSOR.is_pressed():
                sleep(0.01)
        sleep(0.01)
    return


def getInputByTouchSensors():
    global arr
    while True:
        print("Must Enter 25 Numbers! Only 0s and 1s! At most 15 1s!")
        #Define the threads
        button0CheckingSystem = Thread(target=button0Checking)
        button1CheckingSystem = Thread(target=button1Checking)
        
        #Start the threads
        button0CheckingSystem.start()
        button1CheckingSystem.start()
        
        #Keep running until 25 elements have been acquired
        while (numElements[0] < 25) :
            sleep(0.01)
            
        button0CheckingSystem.join()
        button1CheckingSystem.join()
        
        
        if (len(arr) == 25 and numElements[1] <= 15):
            break
        arr = []
        numElements[0] = 0
        numElements[1] = 0
        print("Invalid Input! Start Over!")
    return arr