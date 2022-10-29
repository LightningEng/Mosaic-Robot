#!/usr/bin/env python3

"""
Module to play sounds when ultrasonic sensor detects object within hot-encoded ranges.
This file must be run on the robot.
"""

from utils import sound
from utils.brick import TouchSensor, EV3UltrasonicSensor, wait_ready_sensors, reset_brick
from time import sleep



DELAY_SEC = 0.01  # seconds of delay between measurements
SOUND = sound.Sound(duration=0.3, pitch="A4", volume=60)

print("Program start.\nWaiting for sensors to turn on...")

TOUCH_SENSOR = TouchSensor(2)
US_SENSOR = EV3UltrasonicSensor(4)


wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.
print("Done waiting.")


def play_sound(x):
    
    #Determine flute note to play

    if 0 <= x and x <= 10:
        SOUND = sound.Sound(duration=0.3, pitch="A4", volume=100)
    elif 10 < x and x <= 20:
        SOUND = sound.Sound(duration=0.3, pitch="B4", volume=100)
    elif 20 < x and x <= 30:
        SOUND = sound.Sound(duration=0.3, pitch="C4", volume=100)
    elif 30 < x:
        SOUND = sound.Sound(duration=0.3, pitch="D4", volume=100)
        
    #Play a single note
    SOUND.play()
    SOUND.wait_done()


def digitalFluteMechanism():
    "Produce flute notes based on data from the ultrasonic sensor when activated by button presses."
    try:
        
        print("DFM Activated")
        
        while True:
        
            while not TOUCH_SENSOR.is_pressed():
                pass  # do nothing while waiting for first button press
            print("Digital Flute Activated")
            sleep(1)
            
            while not TOUCH_SENSOR.is_pressed(): #while activated
                us_data = US_SENSOR.get_value()  # Float value in centimeters 0, capped to 255 cm
                if us_data is not None: # If None is given, then data collection failed that time
                    play_sound(x) #play flute note
                sleep(DELAY_SEC)
            
            #deactivated
            print("Digital Flute Deactivated")

    except BaseException:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
        pass
    
    finally:
        print("DFM Deactivated")
        reset_brick() # Turn off everything on the brick's hardware, and reset it
        exit()

if __name__ == "__main__":
    digitalFluteMechanism()