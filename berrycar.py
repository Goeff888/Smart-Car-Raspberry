#coding:utf-8
#Hauptpogramm zum Steuern des Robotors
#berrycar.py
#Christian Göhler
#14.11.2017

import led_progs as LED
import socket_progs as SOCKETS
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

leds = LED.LEDS(LED0,LED1,LED2)
SOCKETS.create_socket()
SOCKETS.bind_socket()
SOCKETS.socket_accept()
leds.initial_blink()
time.sleep (2)

#alle Objekte wieder freigeben
del leds