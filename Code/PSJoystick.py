import RPi.GPIO as GPIO
import time

from pyPS4Controller.controller import Controller
from Motor_Config import MotorControl



class MyController(Controller):

    def __init__(self,motors_dico, **kwargs):
        Controller.__init__(self, **kwargs)
        self.MC=motors_dico
        self.incre=0
        

    def on_x_press(self):
        print("on_x_press")
        self.MC["motor_base"].move_min()
        
    def on_x_release(self):
        print("on_x_release")
        self.MC["motor_base"].stop_now()
        
    def on_triangle_press(self):
        print("on_triangle_press")
        self.MC["motor_base"].move_max()

    def on_triangle_release(self):
        print("on_triangle_release")
        self.MC["motor_base"].stop_now()


    def on_circle_press(self):
        print("on_circle_press")
        self.MC["motor_pince"].move_min()
        
    def on_circle_release(self):
        print("on_circle_release")
        self.MC["motor_pince"].stop_now()
        
        
    def on_square_press(self):
        print("on_square_press")
        self.MC["motor_pince"].move_max()

    def on_square_release(self):
        print("on_square_release")
        self.MC["motor_pince"].stop_now()
        
        
        
    def on_L3_up(self, value):
        print("on_L3_up")

    def on_L3_down(self, value):
        print("on_L3_down")
    
    def on_L3_left(self, value):
        print("on_L3_left ")

    def on_L3_right(self, value):
        print("on_L3_right ")

    def on_L3_y_at_rest(self):
        """L3 joystick is at rest after the joystick was moved and let go off"""
        print("on_L3_y_at_rest")

    def on_L3_x_at_rest(self):
        """L3 joystick is at rest after the joystick was moved and let go off"""
        print("on_L3_x_at_rest")
        
        
        
        
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
        
