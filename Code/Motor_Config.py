import RPi.GPIO as GPIO
import time

class MotorControl:
    def __init__(self,gpio_motor,initpos=0,pos_min=15,pos_max=75,frequency=300):
        GPIO.setmode(GPIO.BCM)
        
        #Motor1
        #variable set
        self.pos_min=pos_min
        self.pos_max=pos_max

        #PWM Intialisation
        servo_pin = gpio_motor
        GPIO.setup(servo_pin, GPIO.OUT)
        self.motor = GPIO.PWM(servo_pin, frequency)
        self.motor.start(initpos)
        self.position=initpos

        #Put the PWM to 0 so the motor doesn't vibrate
        
            

    def move_motor(self,value):
        self.motor.ChangeDutyCycle(value)

    def move_max1(self):
        self.motor.ChangeDutyCycle(self.pos_max)

    def move_min1(self):
        self.motor.ChangeDutyCycle(self.pos_min)
        
    def move_max(self):
        if self.position<self.pos_max :
            self.position+=1
        self.motor.ChangeDutyCycle(self.position)
        time.sleep(0.02)
        print(self.position)

    def move_min(self):
        if self.position>self.pos_min :
            self.position-=1
        self.motor.ChangeDutyCycle(self.position)
        time.sleep(0.02)
        print(self.position)

    def stop_now(self):
        self.motor.ChangeDutyCycle(0)
