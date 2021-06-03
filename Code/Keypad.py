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
        self.press_function= [self.key_1,self.key_4,self.key_7,self.key_etoile,
                              self.key_2,self.key_5,self.key_8,self.key_0,
                              self.key_3,self.key_6,self.key_9,self.key_diez,
                              self.key_A,self.key_B,self.key_C,self.key_D]
        self.unpress_function= [self.unkey_1,self.unkey_4,self.unkey_7,self.unkey_etoile,
                                self.unkey_2,self.unkey_5,self.unkey_8,self.unkey_0,
                                self.unkey_3,self.unkey_6,self.unkey_9,self.unkey_diez,
                                self.unkey_A,self.unkey_B,self.unkey_C,self.unkey_D]
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
                        
                        #self.press_function[pressed_key](self.nombreused[pressed_key])
                        
                        print("pressed :",self.nombreused[pressed_key])
        
                        while(which_col[col_number]!=0):
                            self.press_function[pressed_key](self.nombreused[pressed_key])
                            which_col[col_number]= GPIO.input(self.adresseCol[col_number])
                            
                        self.unpress_function[pressed_key](self.nombreused[pressed_key])
                        
                        time.sleep(0.5)
                        row_number=4
                    row_number=row_number+1
            if col_number==3 :
                col_number=0
            else :
                col_number+=1
                
    def do_none(self,var):
        print("unpressed : ",var)
        
        
    #Controle de la Base
    def key_6(self,var):
        self.MC["motor_base"].move_min1()
        
    def key_4(self,var):
        self.MC["motor_base"].move_max1() 
        
    def unkey_4(self,var):
        self.MC["motor_base"].stop_now()
        
    def unkey_6(self,var):
        self.MC["motor_base"].stop_now()        
        
    #Controle Articulation 1        
    def key_2(self,var):
        self.MC["motor_art_1"].move_min()
    
    def key_8(self,var):
        self.MC["motor_art_1"].move_max()
        
    def unkey_8(self,var):
        #self.MC["motor_art_1"].stop_now()
        pass
    
    def unkey_2(self,var):
        #self.MC["motor_art_1"].stop_now()
        pass
        

        
    #Controle Articulation 2
    def key_1(self,var):
        self.MC["motor_art_2"].move_min()

    def key_7(self,var):
        self.MC["motor_art_2"].move_max()
        
    def unkey_1(self,var):
        #self.MC["motor_art_2"].stop_now()   
        pass

    def unkey_7(self,var):
        #self.MC["motor_art_2"].stop_now()
        pass


    
    #Controle de la Pince
    def key_B(self,var):
        self.MC["motor_pince"].move_max1()

    def key_A(self,var):
        self.MC["motor_pince"].move_min1() 
    
    def unkey_A(self,var):
        self.MC["motor_pince"].move_motor(7)

    def unkey_B(self,var):
        self.MC["motor_pince"].stop_now()
        
        
    #Connection a la manette
    def key_C(self,var):
        print("Bluetooth connection")
        try :
            os.system("bash /home/pi/connect.sh")
            controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=True,motors_dico=self.MC)
            controller.listen(timeout=10)
        except:
            print("no more Bluetooth connection")
    
    #relache tout les moteurs
    def key_5(self,var):
        self.MC["motor_base"].stop_now()
        self.MC["motor_art_1"].stop_now()
        self.MC["motor_art_2"].stop_now()
        self.MC["motor_pince"].stop_now()
        
       
    def key_diez(self,var):
        pass       
    def key_3(self,var):
        pass       
    def key_etoile(self,var):
        pass       
    def key_0(self,var):
        pass       
    def key_9(self,var):
        pass              
    def key_D(self,var):
        pass  
    
    def unkey_diez(self,var):
        pass       
    def unkey_3(self,var):
        pass       
    def unkey_0(self,var):
        pass       
    def unkey_etoile(self,var):
        pass       
    def unkey_9(self,var):
        pass              
    def unkey_D(self,var):
        pass
    def unkey_5(self,var):
        pass
    def unkey_C(self,var):
        pass

