from Motor_Config import MotorControl
from PSJoystick import MyController

def init_all():
    base_motor=MotorControl(gpio_motor=27,initpos=8.5)
    art1_motor=MotorControl(gpio_motor=17)
    
    motorDict= {
        "motor_base":base_motor,
        "motor_art_1":art1_motor
        }
    
    controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=True,motorsDico=motorDict)
    controller.listen()
    
if __name__=="__main__":
    init_all()

    
