from pyPS4Controller.controller import Controller
import RPi.GPIO as GPIO
import time



class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
                
    def on_x_press(self):
        servoPIN = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servoPIN, GPIO.OUT)
        p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
        p.start(2.5) # Initialization
        print("Hello world")
        p.ChangeDutyCycle(5)
        time.sleep(0.5)

    def on_x_release(self):
        print("Goodbye world")
        p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
        p.ChangeDutyCycle(12)
        time.sleep(0.5)



controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=True)
controller.listen()