#coding:utf-8
#drive_progs.py
#Christian Goehler
#14.11.2017
#Ansteuern der LEDS


import berrycar
#import threading

print '....LED START!!!...'

class LEDS(object):
	def __init__(self, led0,led1,led2):
		self.led0 = led0
		self.led1 = led1
		self.led2 = led2
		
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.led0,GPIO.OUT,initial=GPIO.HIGH)
		GPIO.setup(self.led1,GPIO.OUT,initial=GPIO.HIGH)
		GPIO.setup(self.led2,GPIO.OUT,initial=GPIO.HIGH)
####################################################
#Lichter am Board in Reihenfolge leuchten lassen
####################################################		
	def initial_blink(self):
		print ("initial_blink")
		for i in range(1, 5):
			GPIO.output(self.led0,True)
			GPIO.output(self.led1,False)
			GPIO.output(self.led2,False)
			print ("Test1")
			time.sleep(0.5)
			GPIO.output(self.led0,True)
			GPIO.output(self.led1,True)
			GPIO.output(self.led2,False)
			print ("Test2")
			time.sleep(0.5)
			GPIO.output(self.led0,True)
			GPIO.output(self.led1,True)
			GPIO.output(self.led2,True)
			print ("Test3")
			time.sleep(0.5)
			GPIO.output(self.led0,False)
			GPIO.output(self.led1,False)
			GPIO.output(self.led2,False)
			print ("Test4")
	
#Fubktion nicht hier verwenden da sonst alles aufgeräumnt wird	
	#def __del__(self):	
		#GPIO.cleanup()
####################################################		
#Lichter für die Motorrichtung
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









