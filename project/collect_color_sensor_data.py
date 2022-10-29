#!/usr/bin/env python3

"""
This test is used to collect data from the color sensor.
It must be run on the robot.
"""

# Add your imports here, if any
from utils.brick import EV3ColorSensor, wait_ready_sensors, TouchSensor, reset_brick

from time import sleep



COLOR_SENSOR_DATA_FILE = "../data_analysis/color_sensor.csv"

# complete this based on your hardware setup
EV3COLOR_SENSOR = EV3ColorSensor(2)
COLOR_TOUCH_SENSOR = TouchSensor(1)



wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.


def collect_color_sensor_data():
    #"Collect color sensor data."
    
   #try:
        output_file = open(COLOR_SENSOR_DATA_FILE, "a")  #"open the output file"
        running = True
        
        #"Continuously samples the color sensor"
        
        while not COLOR_TOUCH_SENSOR.is_pressed(): 
             pass# do nothing while waiting for first button press
        
        #color_data = EV3COLOR_SENSOR.get_rgb()
        #print(color_data)
        #output_file.write(f"{color_data}\n")
        #firstTime = True
        while running:        
            #print(color_data)
            output_file = open(COLOR_SENSOR_DATA_FILE, "a")
            read_touch = COLOR_TOUCH_SENSOR.is_pressed()
            if (read_touch == True):
                color_data = EV3COLOR_SENSOR.get_rgb()
                sleep(0.5)
                print(color_data)
                output_file.write(f"{color_data}\n")
                output_file.close()
                #firstTime = False
#         print("Color touch sensor pressed")
#         
#         print("Starting to collect color samples")
#         
#         while COLOR_TOUCH_SENSOR.is_pressed():
#             print("hello")
#             color_data = EV3COLOR_SENSOR.get_rgb()
#             print(color_data)
#             output_file.write(f"{color_data}\n")
#                 if color_data is not [None,None,None,None]:  # If None is given, then data collection failed that time
#                     print(color_data)
#                     output_file.write(f"{color_data}\n")
#                 sleep(0.1)
    #except BaseException:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
         #print("Error, system crashed")
         #pass
    #finally:
         #print("Done collecting Color sensor data samples")
         #output_file.close()
         #reset_brick() # Turn off everything on the brick's hardware, and reset it
         #exit()
        
    
        
    
    #"An action to write the color sensor reading to the output file when conditions are met."
    

if __name__ == "__main__":

    collect_color_sensor_data()
