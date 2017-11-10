#coding:utf-8


from socket import *
from time import ctime
import binascii		#f?r Geschwindigkeit
import RPi.GPIO as GPIO
import time
import threading
from smbus import SMBus
#import smbus

#bus = smbus.SMBus(1)

XRservo = SMBus(1)
print '....WIFIROBOTS START!!!...'


#####Borad-Modus festlegen###################
GPIO.setmode(GPIO.BCM)

########LED-Belegung am Treiberboard#################
LED0 = 10
LED1 = 9
LED2 = 25



########Motor-Pinbelegung################
ENA = 13	#//L298 A
ENB = 20	#//L298 B
IN1 = 19	#//INI1
IN2 = 16	#//INI2
IN3 = 21	#//INI3
IN4 = 26	#//INI4


#######################################
GPIO.setwarnings(True)
GPIO.cleanup()
#########LEDS initialisieren##########
GPIO.setup(LED0,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(LED1,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(LED2,GPIO.OUT,initial=GPIO.HIGH)

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
#init_light()
#Lichter am Board in Reihenfolge leuchten lassen
####################################################
def	init_light():#???
	for i in range(1, 5):
		GPIO.output(LED0,True)#
		GPIO.output(LED1,False)#
		GPIO.output(LED2,False)#
		time.sleep(0.5)
		GPIO.output(LED0,True)#
		GPIO.output(LED1,True)#
		GPIO.output(LED2,False)#
		time.sleep(0.5)
		GPIO.output(LED0,True)#
		GPIO.output(LED1,True)#
		GPIO.output(LED2,True)#
		time.sleep(0.5)
		GPIO.output(LED0,False)#
		GPIO.output(LED1,False)#
		GPIO.output(LED2,False)
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
def Motor_Init():
	print 'Testen der Motorrichtungen'
	Motor_Forward()
	time.sleep(2)
	Motor_Stop()
	Motor_Backward()
	time.sleep(2)
	Motor_Stop()
	Motor_TurnLeft()
	time.sleep(2)
	Motor_Stop()
	Motor_TurnRight()
	time.sleep(2)
	Motor_Stop()
	
##########Websocket-Server startetn###########################	
def Connecttion_Init():
	print 'Starten des Socketservers'
#tbd
	print 'Kamerverbindung aktivieren'
	
#XRservo.XiaoRGEEK_SetServo(0x01,10)

init_light()
Motor_Init()
Connecttion_Init()




GPIO.cleanup()
