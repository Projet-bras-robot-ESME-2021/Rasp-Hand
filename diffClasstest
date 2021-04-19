from pyPS4Controller.controller import Controller
import RPi.GPIO as GPIO
import time



class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        self.whichbut=None
        
    def on_x_press(self):
        print("on_x_press")
        self.whichbut="x"

    def on_x_release(self):
        print("on_x_release")
        self.whichbut=None

    def on_triangle_press(self):
        print("on_triangle_press")
        self.whichbut="triangle"

    def on_triangle_release(self):
        print("on_triangle_release")
        self.whichbut=None

    def on_circle_press(self):
        print("on_circle_press")

    def on_circle_release(self):
        print("on_circle_release")

    def on_square_press(self):
        print("on_square_press")

    def on_square_release(self):
        print("on_square_release")
        
    def on_up_arrow_press(self):
        print("on_up_arrow_press")

    def on_up_down_arrow_release(self):
        print("on_up_down_arrow_release")

    def on_down_arrow_press(self):
        print("on_down_arrow_press")

    def on_left_arrow_press(self):
        print("on_left_arrow_press")

    def on_left_right_arrow_release(self):
        print("on_left_right_arrow_release")

    def on_right_arrow_press(self):
        print("on_right_arrow_press")


class Motor_Control(MyController):
    def __init__(self, **kwargs):
        controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=True)
        controller.listen()
        servoPIN = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servoPIN, GPIO.OUT)
        self.p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
        self.p.start(2.5) # Initialization
        
    def whichone(self):
        if controller.whichbut =="x":
            print("yes it works")
        elif controller.whichbut =="triangle":
            print("don't worry it works")
        


MC=Motor_Control()
MC.whichone()
