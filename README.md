# Sensors and Testing

_Read this entire document before doing anything._

In this lab, we will test the robot sensors to learn how they can be used in an
application, eg, a musical instrument.

## Setup

You will have 2 main options to develop code:

- **Option 1: Simple Setup:** Follow the **Getting Started Guide** found in MyCourses under **Content > Tutorials > Tutorial 3**

- **Option 2: Advanced Setup:** Follow the **Getting Started Guide** AND the other guide [advanced-setup.md](./flexible-setup.md)

- **Option 2: MORE Advanced Setup:** Follow the **Getting Started Guide** AND the other guide **Advanced Git File Transfer** in MyCourses under **Content > Tutorials > Tutorial 3**

Choose Option 1 if you are indecisive.

___

**In both cases, also do the following:**

**On the brick:** Double-click `robot_setup.sh` and select "Run in terminal"
to install the simpleaudio library.

**On your computer/laptop:** Run this command in the terminal to install
matplotlib, a library for plotting graphs:

```
python3 -m pip install matplotlib
```
___










# Extra Information:

## Project Organization

In this section, we go over the files and folders included in this lab,
listed in alphabetical order.
The files you need to modify are shown in **bold**.

- `data_analysis`
  - [`us_sensor_cont_visualization.py`](data_analysis/us_sensor_cont_visualization.py):
  visualize the distance measurements
  collected by the ultrasonic sensor. Run this on your computer.
  You are allowed to modify this file, eg, to change the plot color,
  but you are not required to.
  - [`color_sensor_visualization.py`](data_analysis/color_sensor_visualization.py):
  visualize the color measurements collected by the color sensor as
  RGB intensity Gaussian distributions, as shown in class. Run this on your computer.
- `lib`: contains the simpleaudio sound library.
- `project`: all Python files in this folder run on the robot.
  - [`doc`](project/doc): documentation for the brick API
  (Application Programming Interface), ie, the classes and functions
  you can use to work with the robot.
  - [`utils`](project/utils): brick-related utilities for this project.
  See the other project files to see examples of how to use these modules.
    - `brick.py`: the main module for interacting with the brick hardware.
    - `sound.py`: module that allows you to play sounds.
    It depends on the simpleaudio library.
  - [**`collect_color_sensor_data.py`**](project/collect_color_sensor_data.py):
  a script to collect data from the color sensor.
  **Complete the function definition in this file.**
  - [**`collect_us_sensor_data.py`**](project/collect_us_sensor_data.py):
  a script to collect data from the ultrasonic sensor.
  **Just use this file to collect data. It is complete.**
  - [**`speaker_button.py`**](project/speaker_button.py):
  a script to play music when the speaker button is pressed.
  **Complete the function definition in this file.**
- `scripts`:
  - `reset_brick.py`: If your program does not exit correctly, eg,
  if you are stuck in an infinite loop, run this script on the brick to reset it.
- `deploy_to_robot.py`: a script to deploy the code to the robot from your computer.
  It offers the following options:
  - Deploy DPM Project on Robot without running:
  copy the `lab2` folder to the robot.
  - Deploy and run DPM Project on Robot:
  copy the `lab2` folder to the robot and run the file specified
  in `project_info.json`.
  - Reset Robot: reset the robot.
- **`project_info.json`**: a file containing information about the project.
- `robot_setup.sh`: a script to install the simpleaudio library on
the brick as described above.

