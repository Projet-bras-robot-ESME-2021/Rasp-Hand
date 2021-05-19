from Motor_Config import MotorControl
from Keypad import Keypad
import os

def init_all():
    base_motor=MotorControl(gpio_motor=27,initpos=8.5)
    pince_motor=MotorControl(gpio_motor=17,initpos=8.5)
    art1_motor=MotorControl(gpio_motor=22)
    art2_motor=MotorControl(gpio_motor=10)
    
    motor_dict= {
        "motor_base":base_motor,
        "motor_pince":pince_motor,
        "motor_art_1":art1_motor,
        "motor_art_2":art2_motor
    }
    
    os.system("bash connect.sh")
    key=Keypad(motors_dico=motor_dict)
    key.listener()
    
    
if __name__=="__main__":
    init_all()

    
