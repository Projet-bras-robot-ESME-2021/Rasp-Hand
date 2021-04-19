from pyPS4Controller.controller import Controller
import RPi.GPIO as GPIO
import time

class MotorContral:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        
        #Motor1
        servo1PIN = 17
        GPIO.setup(servo1PIN, GPIO.OUT)
        self.Motor1 = GPIO.PWM(servo1PIN, 50)
        self.Motor1.start(10) 

        #Motor2
        servo2PIN = 17
        GPIO.setup(servo2PIN, GPIO.OUT)
        self.Motor2 = GPIO.PWM(servo2PIN, 50)
        self.Motor2.start(10)
        
    def MoveMotor1(self,value):
        self.Motor1.ChangeDutyCycle(value)
        
    def MoveMotor2(self,value):
        self.Motor2.ChangeDutyCycle(value)
        
    def StopNow(self):
        self.Motor1.ChangeDutyCycle(0)
        self.Motor2.ChangeDutyCycle(0)
        
MC=MotorControl()

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        
        
    def on_x_press(self):
        print("on_x_press")
        MC.MoveMotor1(4)

    def on_x_release(self):
        print("on_x_release")
        MC.StopNow()
        
    def on_triangle_press(self):
        print("on_triangle_press")
        MC.MoveMotor1(20)

    def on_triangle_release(self):
        print("on_triangle_release")
        MC.StopNow()

    def on_circle_press(self):
        print("on_circle_press")
        MC.MoveMotor2(4)

    def on_circle_release(self):
        print("on_circle_release")
        MC.StopNow()

    def on_square_press(self):
        print("on_square_press")
        MC.MoveMotor2(20)

    def on_square_release(self):
        print("on_square_release")
        MC.StopNow()
        
        
        
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
        



controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=True)
controller.listen()
