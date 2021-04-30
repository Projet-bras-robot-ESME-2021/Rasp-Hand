from Motor_Config import MotorControl
from PSJoystick import MyController

def init_all():
    motor_Base=MotorControl(GPIO_Motor=27,initpos=8.5)
    motor_Art1=MotorControl(GPIO_Motor=17)
    
    motorDict= {
        "MotorBase":motor_Base,
        "MotorArt1":motor_Art1
        }
    
    controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=True,motorsDico=motorDict)
    controller.listen()
    
if __name__=="__main__":
    init_all()

    