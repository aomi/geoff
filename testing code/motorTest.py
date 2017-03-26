import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
 #determining what pins the motors are controlled by
 #A and B control direction while E is enable
motor1A = 33
motor1B = 31
motor1E = 29

motor2A = 40
motor2B = 38
motor2E = 36

#setting as outputs
GPIO.setup(motor1A,GPIO.OUT)
GPIO.setup(motor1B,GPIO.OUT)
GPIO.setup(motor1E,GPIO.OUT)
GPIO.setup(motor2A,GPIO.OUT)
GPIO.setup(motor2B,GPIO.OUT)
GPIO.setup(motor2E,GPIO.OUT)
 
print "Turning motor on"
GPIO.output(motor2A,GPIO.HIGH)
GPIO.output(motor2B,GPIO.LOW)
GPIO.output(motor2E,GPIO.HIGH)
 
sleep(2)
 
print "Stopping motor"
GPIO.output(motor2E,GPIO.LOW)
 
GPIO.cleanup()
