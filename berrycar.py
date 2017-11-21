#coding:utf-8
#Hauptpogramm zum Steuern des Robotors
#berrycar.py
#Christian Göhler
#14.11.2017
import RPi.GPIO as GPIO
import time
import socket
#import sys
#import led_progs as LED
import drive_progs as DRIVE

#import socket_progs 
#import drive_progs as DRIVE
import time

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

class Drive(object):
	def __init__(self, en,in1,in2):
		self.en = en
		self.in1 = in1
		self.in2 = in2
		
		print '....MOTOR START!!!...'
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.en,GPIO.OUT,initial=GPIO.LOW)
		GPIO.setup(self.in1,GPIO.OUT,initial=GPIO.LOW)
		GPIO.setup(self.in2,GPIO.OUT,initial=GPIO.LOW)
		self.EN_pwm=GPIO.PWM(en,1000)
		self.EN_pwm.ChangeDutyCycle(50)	################
####################################################
#Motoransteuerung
#Die Fahrtrichtung muss im Hauptprogramm über gegensätzliches Setzen der beiden Motorobjekte
####################################################		
	def Motor_Forward(self):
		print 'motor forward'
		GPIO.output(self.en,True)	
		GPIO.output(self.in1,True)
		GPIO.output(self.in2,False)
	def Motor_Backward(self):
		print 'motor forward'
		GPIO.output(self.en,True)	
		GPIO.output(self.in1,False)
		GPIO.output(self.in2,True)
	def Motor_Stop(self):
		print 'motor_stop'
		GPIO.output(self.en,False)	
		GPIO.output(self.in1,False)
		GPIO.output(self.in2,False)
	
	def ENA_Speed(EA_num):
		speed=hex(eval('0x'+EA_num))
		speed=int(speed,16)
		print 'EA_A??? %d '%speed
		#self.EN_pwm.ChangeDutyCycle(speed)

#leds = LED.LEDS(LED0,LED1,LED2)
#leds.initial_blink()
time.sleep (2)

engines_left = DRIVE.Drive(ENA,IN1,IN2)
engines_right = DRIVE.Drive(ENB,IN3,IN4)
engines_left.Motor_Forward()
engines_right.Motor_Forward()
time.sleep (1)
engines_left.Motor_Stop()
engines_right.Motor_Stop()
#SOCKETS.create_socket()
#SOCKETS.bind_socket()
#SOCKETS.socket_accept()

#leds.initial_blink()
#time.sleep (2)

#alle Objekte wieder freigeben
#del leds
#del SOCKETS