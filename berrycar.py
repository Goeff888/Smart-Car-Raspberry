#coding:utf-8
#Hauptpogramm zum Steuern des Robotors
#berrycar.py
#Christian Göhler
#14.11.2017
import RPi.GPIO as GPIO
import time
import socket
import sys
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