from Motor_Config import MotorControl
from Keypad import Keypad
from PSJoystick import MyController
import os

def init_all():
    base_motor=MotorControl(gpio_motor=17,pos_max=9,pos_min=5,frequency=50)
    art1_motor=MotorControl(gpio_motor=27)
    art2_motor=MotorControl(gpio_motor=22)
    pince_motor=MotorControl(gpio_motor=10,pos_max=9,pos_min=5,frequency=50)
    
    motor_dict= {
        "motor_base":base_motor,
        "motor_art_1":art1_motor,
        "motor_art_2":art2_motor,
        "motor_pince":pince_motor,
    }

    key=Keypad(motors_dico=motor_dict)
    key.listener()
    
    #controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=True,motors_dico=motor_dict)
    #controller.listen(timeout=10)
    
    
if __name__=="__main__":
    init_all()

