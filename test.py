from pyPS4Controller.controller import Controller
import RPi.GPIO as GPIO
import time



class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        servoPIN = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servoPIN, GPIO.OUT)
        self.p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
        self.p.start(2.5) # Initialization
        
    def on_x_press(self):
        
        print("Hello world")
        self.p.ChangeDutyCycle(5)
        

    def on_square_press(self):
        print("Goodbye world")
        self.p.ChangeDutyCycle(12)
        



controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=True)
controller.listen()