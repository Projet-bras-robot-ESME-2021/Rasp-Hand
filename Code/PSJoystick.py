import RPi.GPIO as GPIO
import time

from pyPS4Controller.controller import Controller
from Motor_Config import MotorControl



class MyController(Controller):

    def __init__(self,motorsDico, **kwargs):
        Controller.__init__(self, **kwargs)
        self.MC=motorsDico
        self.incre=0
        
    def on_x_press(self):
        print("on_x_press")
        self.MC["MotorArt1"].MoveMotor(4)
        

    def on_x_release(self):
        print("on_x_release")
        self.MC["MotorArt1"].StopNow()
        
    def on_triangle_press(self):
        print("on_triangle_press")
        self.MC["MotorArt1"].MoveMotor(15)

    def on_triangle_release(self):
        print("on_triangle_release")
        self.MC["MotorArt1"].StopNow()

    def on_circle_press(self):
        print("on_circle_press")
        self.MC["MotorBase"].MoveMotor(4)

    def on_circle_release(self):
        print("on_circle_release")
        self.MC["MotorBase"].StopNow()

    def on_square_press(self):
        print("on_square_press")
        self.MC["MotorBase"].MoveMotor(15)

    def on_square_release(self):
        print("on_square_release")
        self.MC["MotorBase"].StopNow()
        
        
        
    def on_L3_up(self, value):
        print("on_L3_up")
        if self.incre>2:
            self.incre-=1
            self.MC["MotorArt1"].MoveMotor(self.incre)

    def on_L3_down(self, value):
        print("on_L3_down")
        if self.incre<12:
            self.incre+=1
            self.MC["MotorArt1"].MoveMotor(self.incre)

    def on_L3_left(self, value):
        print("on_L3_left ")

    def on_L3_right(self, value):
        print("on_L3_right ")

    def on_L3_y_at_rest(self):
        """L3 joystick is at rest after the joystick was moved and let go off"""
        print("on_L3_y_at_rest")
        self.MC["MotorArt1"].StopNow()

    def on_L3_x_at_rest(self):
        """L3 joystick is at rest after the joystick was moved and let go off"""
        print("on_L3_x_at_rest")
        self.MC["MotorArt1"].StopNow()
        
        
        
        
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
        