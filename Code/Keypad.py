import RPi.GPIO as GPIO
import time

class Keypad:
    def __init__(self):
        
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
        self.press_function= [self.do_none,self.turn_left,self.do_none,self.do_none,
                              self.forward,self.do_none,self.backward,self.do_none,
                              self.do_none,self.turn_right,self.do_none,self.do_none,
                              self.do_none,self.do_none,self.do_none,self.do_none]
        self.unpress_function= [self.do_none,self.stop_turn_left,self.do_none,self.do_none,
                                self.stop_forward,self.do_none,self.stop_backward,self.do_none,
                                self.do_none,self.stop_turn_right,self.do_none,self.do_none,
                                self.do_none,self.do_none,self.do_none,self.do_none]
        self.nombreused= ['1','4','7','*',
                          '2','5','8','0',
                          '3','6','9','#',
                          'A','B','C','D']
        
    def listener(self):
        i=0
        j=0

        print("c'est initialisé")

        while i<4:
            value=GPIO.input(self.adresseCol[0])
            value2=GPIO.input(self.adresseCol[1])
            value3=GPIO.input(self.adresseCol[2])
            value4=GPIO.input(self.adresseCol[3])
            valueused = [value, value2, value3, value4]

            if valueused[i]!=0 :
                j=0
                time.sleep(0.1)
                while j<4 :
                    GPIO.output(self.adresseRow[j], GPIO.LOW)
                               
                    valueused[i]= GPIO.input(self.adresseCol[i])
                    if valueused[i]==0 :
                        
                        GPIO.output(self.adresseRow[0], GPIO.HIGH)
                        GPIO.output(self.adresseRow[1], GPIO.HIGH)
                        GPIO.output(self.adresseRow[2], GPIO.HIGH)
                        GPIO.output(self.adresseRow[3], GPIO.HIGH)
                        valueused[i]= GPIO.input(self.adresseCol[i])
                        variable1= i*4 +j
                        
                        self.press_function[variable1]()
                        
                        
                        while(valueused[i]!=0):
                            valueused[i]= GPIO.input(self.adresseCol[i])
                            
                        self.unpress_function[variable1]()
                        
                        time.sleep(0.5)
                        j=4
                    j=j+1
            if i==3 :
                i=0
            else :
                i+=1
                
    def do_none(self):
        pass
                
    def backward(self):
        print("it's gonna move backward")
    
    def forward(self):
        print("it's gonna move forward")
        
    def turn_left(self):
        print("it's gonna move turn_left")
        
    def turn_right(self):
        print("it's gonna move turn_right")
    
    
    
    def stop_all(self):
        print("it stopped")
        
        
   
    def stop_backward(self):
        print("it's gonna stop backward")
    
    def stop_forward(self):
        print("it's gonna stop forward")
        
    def stop_turn_left(self):
        print("it's gonna stop turn_left")
        
    def stop_turn_right(self):
        print("it's gonna stop turn_right")
        
    
                

key=Keypad()
key.listener()
