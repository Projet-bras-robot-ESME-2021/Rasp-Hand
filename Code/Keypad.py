import RPi.GPIO as GPIO
import time

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


adresseRow=[Row1,Row2,Row3,Row4]
adresseCol=[Col1, Col2, Col3, Col4]
nombreused= ['1','4','7','*','2','5','8','0','3','6','9','#','A','B','C','D']
i=0
j=0

print("c'est initialisé")

while i<4:
    value=GPIO.input(Col1)
    value2=GPIO.input(Col2)
    value3=GPIO.input(Col3)
    value4=GPIO.input(Col4)
    valueused = [value, value2, value3, value4]

    if valueused[i]!=0 :
        j=0
        time.sleep(0.1)
        while j<4 :
            GPIO.output(adresseRow[j], GPIO.LOW)
                       
            valueused[i]= GPIO.input(adresseCol[i])
            if valueused[i]==0 :
                
                GPIO.output(Row1, GPIO.HIGH)
                GPIO.output(Row2, GPIO.HIGH)
                GPIO.output(Row3, GPIO.HIGH)
                GPIO.output(Row4, GPIO.HIGH)
                valueused[i]= GPIO.input(adresseCol[i])
                variable1= i*4 +j
                texte1=nombreused[variable1]
                print("pressed",texte1)
                
                while(valueused[i]!=0):
                    valueused[i]= GPIO.input(adresseCol[i])
                print("released",texte1)
                time.sleep(0.5)
                j=4
            j=j+1
    if i==3 :
        i=0
    else :
        i+=1
        
