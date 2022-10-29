#!/usr/bin/env python3

"""
Module to run the main program
This file must be run on the robot.
"""
from utils import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors, reset_brick
from time import sleep

from threading import Thread

DELAY_SEC = 0.01  # seconds of delay between measurements
MOTOR_DELAY_SEC = 0.01 
INITIAL_POSITION = 0
TARGET_POSITION = 30
MOTOR_POWER = 100

SOUND = sound.Sound(duration=1, pitch="A4", volume=60)

print("Program start.\nWaiting for sensors to turn on...")


DRUM_TOUCH_SENSOR = TouchSensor(1)
FLUTE_TOUCH_SENSOR = TouchSensor(2)
STOP_TOUCH_SENSOR = TouchSensor(3)
US_SENSOR = EV3UltrasonicSensor(4)
MOTOR = Motor("A")
MOTOR.reset_encoder()

wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.
print("Done waiting.")


#functions

def play_flute_sound(x):
    
    #Determine flute note to play
    if 0 <= x and x <= 10:
        SOUND = sound.Sound(duration=1, pitch="A4", volume=100)
        print("A4")
    elif 10 < x and x <= 20:
        SOUND = sound.Sound(duration=1, pitch="B4", volume=100)
        print("B4")
    elif 20 < x and x <= 30:
        SOUND = sound.Sound(duration=1, pitch="C4", volume=100)
        print("C4")
    #elif 30 < x #and x <= 40:
    else:
        SOUND = sound.Sound(duration=1, pitch="D4", volume=100)
        print("D4")
        
    #Play a single note
    SOUND.play()
    SOUND.wait_done()
    

def digitalFluteMechanism():
    "Produce flute notes based on data from the ultrasonic sensor when activated by button presses."
    
    while True:
            if FLUTE_TOUCH_SENSOR.is_pressed():
                us_data = US_SENSOR.get_value()  # Float value in centimeters 0, capped to 255 cm
                if us_data is not None: # If None is given, then data collection failed that time
                    print(us_data)
                    play_flute_sound(us_data) #play flute note
            if STOP_TOUCH_SENSOR.is_pressed(): #if emergency mechanism triggered
                break
    #deactivated
    print("Digital Flute Deactivated")
    

def drum():
    
    #Activate the Motor
    MOTOR.set_limits(MOTOR_POWER)
    
    #Rotate
    MOTOR.set_position_relative(TARGET_POSITION)
    sleep(0.2)
    
    #Rotate the opposite direction
    MOTOR.set_position_relative(-TARGET_POSITION)
    
    #Deactivate the Motor
    MOTOR.set_limits(0)
    sleep(0.2)
    
    
            
    

def drummingMechanism():

     # Flag to indicate if drums are active or not active
    drumming= False

    #Initialize Motor Defaults
    MOTOR.set_position_relative(INITIAL_POSITION)
    
    while True:
        
        #stop if emergency mechanism is triggered
        if STOP_TOUCH_SENSOR.is_pressed():
            print("EMERGENCY! STOP EVERYTHING")
            break
                
        #sets the drumming tag to its opposite boolean value (makes the touch sensor act as a toggle switch)
        if DRUM_TOUCH_SENSOR.is_pressed():
            drumming = not drumming
            print(drumming)
            sleep(0.3)
        
        #makes the robot drum once
        if drumming == True:
            drum()
            


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



def marchingBand():
    try:
        
        input = getInputByKeyboard()
        
        print(input)
        
        
        
#         #Define the threads
#         fluteSubsystem = Thread(target=digitalFluteMechanism)
#         drumSubsystem = Thread(target=drummingMechanism)
#         
#         #Start the threads
#         fluteSubsystem.start()
#         drumSubsystem.start()
#         
#         #Continue running the program until emergency stop button is pressed
#         while not STOP_TOUCH_SENSOR.is_pressed():
#             sleep(DELAY_SEC)
        
    except BaseException:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
        pass
    
    finally:
        sleep(1) #Ensure that all threads are finished (exiting their respective while loop)
        reset_brick() # Turn off everything on the brick's hardware, and reset it
        exit()

if __name__ == "__main__":
    marchingBand()