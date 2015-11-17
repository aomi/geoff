
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

#Motor Variables: Assigned to corrosponding GPIO Pins
winchA = 
winchB =
winchEnable =
leftPropA =
leftPropB =
leftPropEnable =
rightPropA =
rightPropB =
rightPropEnable =

#Motor class and defining Motor functions
class defineMotor(object):

    def __init__(self, pinA, pinB, pinEnable):
        self.pinA = pinA
        self.pinB = pinB
        self.pinEnable = pinEnable
        GPIO.setup(self.pinA,GPIO.OUT)
        GPIO.setup(self.pinB,GPIO.OUT)
        GPIO.setup(self.pinEnable,GPIO.OUT)
    
    #Motor forward/up command
    def forward(self):
        GPIO.output(self.pinA,GPIO.HIGH)
        GPIO.output(self.pinB,GPIO.LOW)
        GPIO.output(self.pinEnable,GPIO.HIGH)
        
    #Motor reverse/down command
    def reverse(self):
        GPIO.output(self.pinA,GPIO.LOW)
        GPIO.output(self.pinB,GPIO.HIGH)
        GPIO.output(self.pinEnable,GPIO.HIGH)
    
    #Motor stop command    
    def stop(self):
        GPIO.output(self.pinA,GPIO.LOW)
        GPIO.output(self.pinB,GPIO.LOW)
        GPIO.output(self.pinEnable,GPIO.LOW)
        
winch = defineMotor(winchA,winchB,winchEnable)
leftProp = defineMotor(leftPropA,leftPropB,leftPropEnable)
rightProp = defineMotor(rightPropA,rightPropB,rightPropEnable)

while True:
    #determine how to read the data sent by computer
    data.read_how_to_move
