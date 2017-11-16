#drive_progs.py
#Christian Göhler
#14.11.2017
#Ansteuern der Motoren für den Antrieb und die Lenkung

import RPi.GPIO as GPIO
import time

import RPi.GPIO as GPIO
import time
#import threading

print '....LED START!!!...'

class LEDS(object):
	def __init__(self, en,in1,in2):
		self.en = en
		self.in1 = in1
		self.in2 = in2
		
		
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.en,GPIO.OUT,initial=GPIO.LOW)
		GPIO.setup(self.in1,GPIO.OUT,initial=GPIO.LOW)
		GPIO.setup(self.in2,GPIO.OUT,initial=GPIO.LOW)
		#self.ENA_pwm=GPIO.PWM(en,1000)
		
####################################################
#Lichter am Board in Reihenfolge leuchten lassen
####################################################		
	def initial_blink(self):

def init_engine():
########Motor-Pinbelegung################
    ENA = 13	#//L298 A
    ENB = 20	#//L298 B
    IN1 = 19	#//INI1
    IN2 = 16	#//INI2
    IN3 = 21	#//INI3
    IN4 = 26	#//INI4
    
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BCM)
    
    #########Treiberboard initialisieren##########
    GPIO.setup(ENA,GPIO.OUT,initial=GPIO.LOW)
    ENA_pwm=GPIO.PWM(ENA,1000) 
    ENA_pwm.start(0) 
    ENA_pwm.ChangeDutyCycle(50)					#Geschwindigkeit Motor A
    GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)

    GPIO.setup(ENB,GPIO.OUT,initial=GPIO.LOW)
    ENB_pwm=GPIO.PWM(ENB,1000) 
    ENB_pwm.start(0) 
    ENB_pwm.ChangeDutyCycle(50)				#Geschwindigkeit Motor B
    GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)
    
####################################################
#Motor_Forward()
#Motorsteuerung
####################################################		
def Motor_Forward():
	print 'motor forward'
	GPIO.output(ENA,True)
	GPIO.output(ENB,True)
	GPIO.output(IN1,True)
	GPIO.output(IN2,False)
	GPIO.output(IN3,True)
	GPIO.output(IN4,False)
	GPIO.output(LED1,False)#LED1?
	GPIO.output(LED2,False)#LED1?
	
def Motor_Backward():
	print 'motor_backward'
	GPIO.output(ENA,True)
	GPIO.output(ENB,True)
	GPIO.output(IN1,False)
	GPIO.output(IN2,True)
	GPIO.output(IN3,False)
	GPIO.output(IN4,True)
	GPIO.output(LED1,True)#LED1?
	GPIO.output(LED2,False)#LED2?
	
def Motor_TurnLeft():
	print 'motor_turnleft'
	GPIO.output(ENA,True)
	GPIO.output(ENB,True)
	GPIO.output(IN1,True)
	GPIO.output(IN2,False)
	GPIO.output(IN3,False)
	GPIO.output(IN4,True)
	GPIO.output(LED1,False)#LED1?
	GPIO.output(LED2,True) #LED2?
def Motor_TurnRight():
	print 'motor_turnright'
	GPIO.output(ENA,True)
	GPIO.output(ENB,True)
	GPIO.output(IN1,False)
	GPIO.output(IN2,True)
	GPIO.output(IN3,True)
	GPIO.output(IN4,False)
	GPIO.output(LED1,False)#LED1?
	GPIO.output(LED2,True) #LED2?
def Motor_Stop():
	print 'motor_stop'
	GPIO.output(ENA,False)
	GPIO.output(ENB,False)
	GPIO.output(IN1,False)
	GPIO.output(IN2,False)
	GPIO.output(IN3,False)
	GPIO.output(IN4,False)
	GPIO.output(LED1,True)#LED1?
	GPIO.output(LED2,True)#LED2?
	
##########Geschwindigkeit###########################
def ENA_Speed(EA_num):
	speed=hex(eval('0x'+EA_num))
	speed=int(speed,16)
	print 'EA_A??? %d '%speed
	ENA_pwm.ChangeDutyCycle(speed)

def ENB_Speed(EB_num):
	speed=hex(eval('0x'+EB_num))
	speed=int(speed,16)
	print 'EB_B??? %d '%speed
	ENB_pwm.ChangeDutyCycle(speed)
	
##########Fahrprogramme###########################	