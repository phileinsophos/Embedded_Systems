''' this program rotates the stepper motor rotor at specific angle 
    it is the integration of Stepper Motor along with an Ultrasonic Sensor,
    Until the distance calcualated by Ultrasonic Sensor is in between 2 and 20 cm,
    the motor will rotate in clockwise direction, whereas when the distance exceeds the
    speified range and is in between 20 and 100 cm, the rotor changes it diretion '''


import time 
import RPi.GPIO as GPIO

# user defined library
import custom_motor

# dont show any warnings on screen
GPIO.setwarnings(False)

# pin configuration mode (BCM - Broadcom board, BOARD - physical pin structure)
GPIO.setmode(GPIO.BCM) 
TRIG = 20                                   #Associate pin 20 to TRIG
ECHO = 21                                   #Associate pin 21 to ECHO
try:
    print "Distance measurement in progress"
    
    GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
    GPIO.setup(ECHO,GPIO.IN)  
    GpioPins = [18, 23, 24, 25]
    # Declare an named instance of class pass a name and type of motor
    time.sleep(0.5)

    # the rotor will keep on rotating until an interrupt is not grnerated
    while(1):
         GPIO.output(TRIG, False)                   #Set TRIG as LOW
        
         time.sleep(2)                              #Delay of 2 seconds

         GPIO.output(TRIG, True)                    #Set TRIG as HIGH
         time.sleep(0.00001)                        #Delay of 0.00001 seconds
         GPIO.output(TRIG, False)                   #Set TRIG as LOW

         while GPIO.input(ECHO)==0:                 #Check whether the ECHO is LOW
             pulse_start = time.time()              #Saves the last known time of LOW pulse

         while GPIO.input(ECHO)==1:                 #Check whether the ECHO is HIGH
             pulse_end = time.time()                #Saves the last known time of HIGH pulse 

         pulse_duration = pulse_end - pulse_start   #Get pulse duration to a variable

         distance = pulse_duration * 17150          #Multiply pulse duration by 17150 to get distance
         distance = round(distance, 2)              #Round to two decimal points


         #Check whether the distance is within range
         # if in range, then perform clockwise rotation, else anti-clockwise
         if distance > 0 and distance < 20:         
            print "Distance:",distance - 0.5,"cm\n"
            new_import.motor_move(GpioPins , 0.0208, 50, False,0)
            time.sleep(0.5)
         elif distance >20 and distance <100:
            print "Distance:",distance - 0.5,"cm \n"
            new_import.motor_move(GpioPins , 0.0208, -50, False,0)
            time.sleep(0.5)  
         else:
           print("Obstacle out of Range \n\n")

except KeyboardInterrupt:
# cleanup GPIO
    GPIO.cleanup()
