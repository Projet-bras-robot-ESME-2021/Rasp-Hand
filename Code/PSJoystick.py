import RPi.GPIO as GPIO
import time

from pyPS4Controller.controller import Controller
from Motor_Config import MotorControl

import os


class MyController(Controller):

    def __init__(self,motors_dico, **kwargs):
        Controller.__init__(self, **kwargs)
        self.MC=motors_dico


    def on_L1_press(self):
        self.MC["motor_pince"].move_min1()

    def on_L1_release(self):
        self.MC["motor_pince"].stop_now()

    def on_R1_press(self):
        self.MC["motor_pince"].move_max1()

    def on_R1_release(self):
        self.MC["motor_pince"].stop_now()
        


    def on_circle_press(self):
        print("on_circle_press")
        self.MC["motor_base"].move_min1()
        
    def on_circle_release(self):
        print("on_circle_release")
        self.MC["motor_base"].stop_now()
        
    def on_square_press(self):
        print("on_square_press")
        self.MC["motor_base"].move_max1()

    def on_square_release(self):
        print("on_square_release")
        self.MC["motor_base"].stop_now()
        
        
        
    
    def on_L3_up(self, value):
        self.MC["motor_art_1"].move_max1()

    def on_L3_down(self, value):
        self.MC["motor_art_1"].move_min1()

    def on_L3_y_at_rest(self):
        print("on_L3_y_at_rest")
        self.MC["motor_art_1"].stop_now()

    def on_L3_x_at_rest(self):
        print("on_L3_x_at_rest")
        self.MC["motor_art_1"].stop_now()
        
        
        
    def on_R3_up(self, value):
        self.MC["motor_art_2"].move_max1()

    def on_R3_down(self, value):
        self.MC["motor_art_2"].move_min1()

    def on_R3_y_at_rest(self):
        print("on_L3_y_at_rest")
        self.MC["motor_art_2"].stop_now()

    def on_R3_x_at_rest(self):
        print("on_L3_x_at_rest")
        self.MC["motor_art_2"].stop_now()
        

    def on_R2_press(self, value):
        if value>0:
            self.MC["motor_art_2"].move_min1()
        elif value<0 :
            self.MC["motor_art_2"].move_max1()
        elif value==0 :
            self.MC["motor_art_2"].stop_now()
        
        print("on_R2_press: {}".format(value))
        
    def on_options_press(self):
        os.system("bash /home/pi/disconnect.sh")
