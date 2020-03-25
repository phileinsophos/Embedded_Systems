import time 
import RPi.GPIO as GPIO
import math 
def motor_move(gpiopins, wait, steps,verbose, initdelay):
    for pin in gpiopins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, False)
    time.sleep(initdelay)
    out1,out2,out3,out4=gpiopins[0],gpiopins[1],gpiopins[2],gpiopins[3]
    GPIO.output(out1,GPIO.LOW)
    GPIO.output(out2,GPIO.LOW)
    GPIO.output(out3,GPIO.LOW)
    GPIO.output(out4,GPIO.LOW)
    if(verbose == True):
        print "this is verbose information"
        print "delay : ",wait," sec"
        print "Number of steps : ",abs(steps)
        print "initial delay before motor execution : ",initdelay
        print "rotation angle : ",abs(steps*1.8)
        print("\n")
        
    if steps>0:
         counter=1
         i=0
         while(counter<steps):
                  if i==0:
                      GPIO.output(out1,GPIO.HIGH)
                      GPIO.output(out2,GPIO.LOW)
                      GPIO.output(out3,GPIO.LOW)
                      GPIO.output(out4,GPIO.LOW)
                      time.sleep(wait)
                      counter+=1
                      i+=1
                    
                  elif i==1:
                      GPIO.output(out1,GPIO.LOW)
                      GPIO.output(out2,GPIO.HIGH)
                      GPIO.output(out3,GPIO.LOW)
                      GPIO.output(out4,GPIO.LOW)
                      time.sleep(wait)
                      counter+=1
                      i+=1
                     
                  elif i==2:  
                      GPIO.output(out1,GPIO.LOW)
                      GPIO.output(out2,GPIO.LOW)
                      GPIO.output(out3,GPIO.HIGH)
                      GPIO.output(out4,GPIO.LOW)
                      time.sleep(wait)
                      counter+=1
                      i+=1
                     
                  elif i==3:    
                      GPIO.output(out1,GPIO.LOW)
                      GPIO.output(out2,GPIO.LOW)
                      GPIO.output(out3,GPIO.LOW)
                      GPIO.output(out4,GPIO.HIGH)
                      time.sleep(wait)
                      counter+=1
                      i=0
    else:
        counter=0
        i=3
        while(counter>steps):
                  if i==0:
                      GPIO.output(out1,GPIO.HIGH)
                      GPIO.output(out2,GPIO.LOW)
                      GPIO.output(out3,GPIO.LOW)
                      GPIO.output(out4,GPIO.LOW)
                      time.sleep(wait)
                      counter-=1
                      i=3
                    
                  elif i==1:
                      GPIO.output(out1,GPIO.LOW)
                      GPIO.output(out2,GPIO.HIGH)
                      GPIO.output(out3,GPIO.LOW)
                      GPIO.output(out4,GPIO.LOW)
                      time.sleep(wait)
                      counter-=1
                      i-=1
                     
                  elif i==2:  
                      GPIO.output(out1,GPIO.LOW)
                      GPIO.output(out2,GPIO.LOW)
                      GPIO.output(out3,GPIO.HIGH)
                      GPIO.output(out4,GPIO.LOW)
                      time.sleep(wait)
                      counter-=1
                      i-=1
                     
                  elif i==3:    
                      GPIO.output(out1,GPIO.LOW)
                      GPIO.output(out2,GPIO.LOW)
                      GPIO.output(out3,GPIO.LOW)
                      GPIO.output(out4,GPIO.HIGH)
                      time.sleep(wait)
                      counter-=1
                      i-=1