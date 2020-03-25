# Embedded-System---Stepper-Motor
This is a simple experimentation with Raspberry Pi, 
which is used to control the execution of stepper motor and ultrasonic sensor.

The project includes 3 python scripts.
1. custom_motor.py :
      this script contains code implementation for activation and deactivation of stator magnetism at each step
      
2. stepper_motor.py :
      this script contains actual stepper motor execting code, 
      which asks the user to enter the specific angle with wich each step should be taken,
      and rotates the motor first in clockwise directioon with provided angle and then in reverse direction
      
3. stepper_ultrasonic.py :
      this file is the integration of both stepper motor and ultrasonic sensor, 
      which makes the system designed to work as a radar system
      
