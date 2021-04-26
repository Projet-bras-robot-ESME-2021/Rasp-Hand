import RPi.GPIO as GPIO
import time

class MotorControl:
    def __init__(self,GPIO_Motor,initpos=0):
        GPIO.setmode(GPIO.BCM)
        
        #Motor1
        servoPIN = GPIO_Motor
        GPIO.setup(servoPIN, GPIO.OUT)
        self.Motor = GPIO.PWM(servoPIN, 50)
        self.Motor.start(initpos)
        if initpos != 0:
            time.sleep(1)
            self.Motor.ChangeDutyCycle(0)
        
    def MoveMotor(self,value):
        self.Motor.ChangeDutyCycle(value)
        
    def StopNow(self):
        self.Motor.ChangeDutyCycle(0)
