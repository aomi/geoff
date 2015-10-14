import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

class defineMotor(object):

    def __init__(self, pinA, pinB, pinEnable):
        self.pinA = pinA
        self.pinB = pinB
        self.pinEnable = pinEnable
        GPIO.setup(self.pinA,GPIO.OUT)
        GPIO.setup(self.pinB,GPIO.OUT)
        GPIO.setup(self.pinEnable,GPIO.OUT)
    
    def forward(self):
        GPIO.output(self.pinA,GPIO.HIGH)
        GPIO.output(self.pinB,GPIO.LOW)
        GPIO.output(self.pinEnable,GPIO.HIGH)
        
motor1 = defineMotor(33,31,29)
motor2 = defineMotor(40,38,36)

motor1.forward()
motor2.forward()

time.sleep(5)

GPIO.cleanup()
