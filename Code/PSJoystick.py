import RPi.GPIO as GPIO
import time

from pyPS4Controller.controller import Controller
from Motor_Config import MotorControl



class MyController(Controller):

    def __init__(self,motors_dico, **kwargs):
        Controller.__init__(self, **kwargs)
        self.MC=motors_dico
        

    def on_x_press(self):
        print("on_x_press")
        self.MC["motor_base"].move_min()
        
    def on_x_release(self):
        print("on_x_release")
        self.MC["motor_base"].stop_now()
        
    def on_triangle_press(self):
        print("on_triangle_press")
        

    def on_triangle_release(self):
        print("on_triangle_release")

    def on_L1_press(self):
        self.MC["motor_pince"].move_min1()

    def on_L1_release(self):
        self.MC["motor_pince"].stop_now()

    def on_R1_press(self):
        self.MC["motor_pince"]. move_max1()

    def on_R1_release(self):
        self.MC["motor_pince"].stop_now()
        


    def on_circle_press(self):
        print("on_circle_press")
        self.MC["motor_base"].move_min()
        
    def on_circle_release(self):
        print("on_circle_release")
        self.MC["motor_base"].stop_now()
        
        
    def on_square_press(self):
        print("on_square_press")
        self.MC["motor_base"].move_max()

    def on_square_release(self):
        print("on_square_release")
        self.MC["motor_base"].stop_now()
        
        
        
    
    def on_L3_up(self, value):
        self.MC["motor_art_1"].move_max()

    def on_L3_down(self, value):
        self.MC["motor_art_1"].move_min()

    def on_L3_y_at_rest(self):
        print("on_L3_y_at_rest")
        self.MC["motor_art_1"].stop_now()

    def on_L3_x_at_rest(self):
        print("on_L3_x_at_rest")
        self.MC["motor_art_1"].stop_now()
        
        
    def on_R3_up(self, value):
        self.MC["motor_art_2"].move_max()

    def on_R3_down(self, value):
        self.MC["motor_art_2"].move_min()

    def on_R3_y_at_rest(self):
        print("on_L3_y_at_rest")
        self.MC["motor_art_2"].stop_now()

    def on_R3_x_at_rest(self):
        print("on_L3_x_at_rest")
        self.MC["motor_art_2"].stop_now()

        
        
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
        
