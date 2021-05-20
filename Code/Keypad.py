import RPi.GPIO as GPIO
import time
import os
from Motor_Config import MotorControl
from PSJoystick import MyController



class Keypad:
    def __init__(self,motors_dico):
        
        self.MC=motors_dico
        
        Row1=14
        Row2=15
        Row3=18
        Row4=23

        Col1=5
        Col2=6
        Col3=13
        Col4=19

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(Row1, GPIO.OUT)
        GPIO.setup(Row2, GPIO.OUT)
        GPIO.setup(Row3, GPIO.OUT)
        GPIO.setup(Row4, GPIO.OUT)

        GPIO.output(Row1, GPIO.HIGH)
        GPIO.output(Row2, GPIO.HIGH)
        GPIO.output(Row3, GPIO.HIGH)
        GPIO.output(Row4, GPIO.HIGH)

        GPIO.setup(Col1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(Col2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(Col3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(Col4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


        self.adresseRow=[Row1,Row2,Row3,Row4]
        self.adresseCol=[Col1, Col2, Col3, Col4]
        self.press_function= [self.do_none,self.key_4,self.do_none,self.do_none,
                              self.key_2,self.do_none,self.key_8,self.do_none,
                              self.do_none,self.key_6,self.do_none,self.do_none,
                              self.do_none,self.key_B,self.do_none,self.do_none]
        self.unpress_function= [self.do_none,self.unkey_4,self.do_none,self.do_none,
                                self.unkey_2,self.do_none,self.unkey_8,self.do_none,
                                self.do_none,self.unkey_6,self.do_none,self.do_none,
                                self.do_none,self.unkey_B,self.do_none,self.do_none]
        self.nombreused= ['1','4','7','*',
                          '2','5','8','0',
                          '3','6','9','#',
                          'A','B','C','D']
        
    def listener(self):
        col_number=0
        row_number=0

        print("c'est initialisé")

        while col_number<4:
            value=GPIO.input(self.adresseCol[0])
            value2=GPIO.input(self.adresseCol[1])
            value3=GPIO.input(self.adresseCol[2])
            value4=GPIO.input(self.adresseCol[3])
            which_col = [value, value2, value3, value4]

            if which_col[col_number]!=0 :
                row_number=0
                time.sleep(0.1)
                while row_number<4 :
                    GPIO.output(self.adresseRow[row_number], GPIO.LOW)
                               
                    which_col[col_number]= GPIO.input(self.adresseCol[col_number])
                    if which_col[col_number]==0 :
                        
                        GPIO.output(self.adresseRow[0], GPIO.HIGH)
                        GPIO.output(self.adresseRow[1], GPIO.HIGH)
                        GPIO.output(self.adresseRow[2], GPIO.HIGH)
                        GPIO.output(self.adresseRow[3], GPIO.HIGH)
                        
                        which_col[col_number]= GPIO.input(self.adresseCol[col_number])
                        pressed_key= col_number*4 +row_number
                        
                        self.press_function[pressed_key](self.nombreused[pressed_key])
                        
                        
                        while(which_col[col_number]!=0):
                            which_col[col_number]= GPIO.input(self.adresseCol[col_number])
                            self.press_function[pressed_key](self.nombreused[pressed_key])
                            
                        self.unpress_function[pressed_key](self.nombreused[pressed_key])
                        
                        time.sleep(0.5)
                        row_number=4
                    row_number=row_number+1
            if col_number==3 :
                col_number=0
            else :
                col_number+=1
                
    def do_none(self,var):
        print("pressed : ",var)
                
    def key_8(self,var):
        print("it's gonna move backward")
    
    def key_2(self,var):
        print("it's gonna move forward")
        
    def key_4(self,var):
        
        self.MC["motor_base"].move_min()
        
    def key_6(self,var):
        
        self.MC["motor_base"].move_max()
    
    def key_B(self,var):
        print("Bluetooth connection")
        try :
            os.system("bash /home/pi/connect.sh")
            controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=True,motors_dico=self.MC)
            controller.listen(timeout=10)
        except:
            print("no more Bluetooth connection")
    
    
    
    def stop_all(self,var):
        print("it stopped")
        
        
   
    def unkey_8(self,var):
        print("it's gonna stop backward")
        self.MC["motor_pince"].stop_now()
    
    def unkey_2(self,var):
        print("it's gonna stop forward")
        self.MC["motor_pince"].stop_now()
        
    def unkey_4(self,var):
        print("it's gonna stop turn_left")
        self.MC["motor_base"].stop_now()
        
    def unkey_6(self,var):
        print("it's gonna stop turn_right")
        self.MC["motor_base"].stop_now()
    
    def unkey_B(self,var):
        pass
        

