import RPi.GPIO as GPIO                           #Import GPIO library
import time                                       #Import time library
GPIO.setmode(GPIO.BCM)                            #Set GPIO pin numbering
PIR = 20                                          #Associate pin 26 to pir
GPIO.setup(PIR, GPIO.IN)                          #Set pin as GPIO in 
print "Waiting for sensor to settle"
time.sleep(2)                                     #Waiting 2 seconds for the sensor to initiate
print "Detecting motion"

try:
	while True:
	   if GPIO.input(PIR):                            #Check whether pir is HIGH
	      print "Motion Detected!"
	      time.sleep(2)                               #D1- Delay to avoid multiple detection
	   else:
	   	  print "No motion!"
	   time.sleep(0.2)                                #While loop delay should be less than detection(hardware) delay

except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C  
    print "break on request!" # print value of counter  

except:  
    # this catches ALL other exceptions including errors.  
    # You won't get any error messages for debugging  
    # so only use it once your code is working  
    print "Other error or exception occurred!"  

finally:  
    GPIO.cleanup() # this ensures a clean exit  