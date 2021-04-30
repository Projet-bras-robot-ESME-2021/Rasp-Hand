import RPi.GPIO as GPIO
import time

class MotorControl:
    def __init__(self,gpio_motor,initpos=0,pos_max=15,pos_min=4):
        GPIO.setmode(GPIO.BCM)
        
        #Motor1
	#variable set
	self.pos_min=pos_min
	self.pos_max=pos_max

	#PWM Intialisation
        servo_pin = gpio_motor
        GPIO.setup(servo_pin, GPIO.OUT)
        self.motor = GPIO.PWM(servo_pin, 50)
        self.motor.start(initpos)

        #Put the PWM to 0 so the motor doesn't vibrate
	if initpos != 0:
            time.sleep(1)
            self.motor.ChangeDutyCycle(0)
        

    def move_motor(self,value):
        self.motor.ChangeDutyCycle(value)

    def move_max(self):
    	self.motor.ChangeDutyCycle(self.pos_max)

    def move_min(self):
    	self.motor.ChangeDutyCycle(self.pos_min)

    def stop_now(self):
        self.motor.ChangeDutyCycle(0)
