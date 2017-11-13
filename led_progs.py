#coding:utf-8



import RPi.GPIO as GPIO
import time
import threading

print '....LED START!!!...'


#####Borad-Modus festlegen###################
GPIO.setmode(GPIO.BCM)

########LED-Belegung am Treiberboard#################
LED0 = 10
LED1 = 9
LED2 = 25

#######################################
GPIO.setwarnings(True)
GPIO.cleanup()
#########LEDS initialisieren##########
GPIO.setup(LED0,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(LED1,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(LED2,GPIO.OUT,initial=GPIO.HIGH)

####################################################
#init_light()
#Lichter am Board in Reihenfolge leuchten lassen
####################################################
def	init_light():
	for i in range(1, 5):
		GPIO.output(LED0,True)
		GPIO.output(LED1,False)
		GPIO.output(LED2,False)
		time.sleep(0.5)
		GPIO.output(LED0,True)
		GPIO.output(LED1,True)
		GPIO.output(LED2,False)
		time.sleep(0.5)
		GPIO.output(LED0,True)
		GPIO.output(LED1,True)
		GPIO.output(LED2,True)
		time.sleep(0.5)
		GPIO.output(LED0,False)
		GPIO.output(LED1,False)
		GPIO.output(LED2,False)
####################################################		
def Motor_Forward():
	print 'motor forward'
	GPIO.output(LED1,False)#LED1?
	GPIO.output(LED2,False)#LED1?
	
def Motor_Backward():
	print 'motor_backward'
	GPIO.output(LED1,True)#LED1?
	GPIO.output(LED2,False)#LED2?
	
def Motor_TurnLeft():
	print 'motor_turnleft'
	GPIO.output(LED1,False)#LED1?
	GPIO.output(LED2,True) #LED2?
def Motor_TurnRight():
	print 'motor_turnright'
	GPIO.output(LED1,False)#LED1?
	GPIO.output(LED2,True) #LED2?
def Motor_Stop():
	print 'motor_stop'
	GPIO.output(LED1,True)#LED1?
	GPIO.output(LED2,True)#LED2?



GPIO.cleanup()
