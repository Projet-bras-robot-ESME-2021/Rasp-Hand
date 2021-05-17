from Motor_Config import MotorControl
from PSJoystick import MyController

def init_all():
    base_motor=MotorControl(gpio_motor=27,initpos=8.5)
    pince_motor=MotorControl(gpio_motor=17,pos_max=12,pos_min=2)
    art1_motor=MotorControl(gpio_motor=22)
    
    motor_dict= {
        "motor_base":base_motor,
        "motor_pince":pince_motor,
        "motor_art_1":art1_motor
	}
    
    controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=True,motors_dico=motor_dict)
    controller.listen()
    
if __name__=="__main__":
    init_all()

    
