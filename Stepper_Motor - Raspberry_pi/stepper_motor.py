''' this program enables execution of a 17HD48008h-22B, 2-phase Bipolar stepper motor
    the motor has 4 input pins, and has a step angle of 1.8 degree
    A L298N driver is used to control the execution of motor'''  

# stepper motor code implementation

import time 
import RPi.GPIO as GPIO

# This code snippet is for Version 1.2 

# import the library, user-created library file
import custom_motor

# ignore and dont show warnings
GPIO.setwarnings(False)   

# set connection mode : BCM (Broadcom board), BOARD(physical board pins)
GPIO.setmode(GPIO.BCM)
GpioPins = [18, 23, 24, 25]

# Declare an named instance of class pass a name and type of motor
time.sleep(0.5)


# get angle for each step or fixed angled rotor movement
# and convert the angle into number of steps as accepted by stepper motor
angle=int(input("Enter Angle "))     
rotation=360/float(angle)   
steps=200/rotation    
rotation=round(rotation)

# rotate the rotor with user-provided angle
# until the total angle formed by the steps is less than 360
while(1):
    # clockwise rotation
    for i in range(int(abs(rotation))):
        new_import.motor_move(GpioPins , 0.0208, int(steps), True,0.0)
        time.sleep(0.5)
    
    # anti-clockwise rotation
    for i in range(int(abs(rotation))):
        new_import.motor_move(GpioPins , 0.0208,int(-steps), True,0.0)
        time.sleep(0.5)


# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()