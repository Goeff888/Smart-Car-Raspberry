#coding:utf-8
#drive_progs.py
#Christian Göhler
#14.11.2017
#Ansteuern der Motoren für den Antrieb und die Lenkung

import RPi.GPIO as GPIO
import time

print '....MOTOR START!!!...'

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



		
