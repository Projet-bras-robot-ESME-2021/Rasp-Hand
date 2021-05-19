from Motor_Config import MotorControl
from PSJoystick import MyController
import os

def init_all():
    base_motor=MotorControl(gpio_motor=27,initpos=8.5)
    pince_motor=MotorControl(gpio_motor=17,initpos=8.5,pos_max=12,pos_min=2)
    art1_motor=MotorControl(gpio_motor=22)
    
    motor_dict= {
        "motor_base":base_motor,
        "motor_pince":pince_motor,
        "motor_art_1":art1_motor
    }
    
    os.system("bash connect.sh")
    controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=True,motors_dico=motor_dict)
    controller.listen(timeout=60)
    
    
       
    
if __name__=="__main__":
    init_all()

    
