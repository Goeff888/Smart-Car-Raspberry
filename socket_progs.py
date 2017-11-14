#coding:utf-8
#socket_progs.py
#Christian Göhler
#14.11.2017
#Socket-Server für die Remote Steuerung über Computer oder Handy

import socket
import sys
 
#Create Connection
def create_socket():
    try:
        global host
        global port
        global s        
        host = ''
        port = 9999     
        s = socket.socket()
    except socket.error as msg:
        print ('Fehler beim Erzeugen eines Sockets' + str (msg))

# Binding den Socket und auf Verbindungen hören
def bind_socket():
    try:
        global host
        global port
        global s
         
        print ('Binding auf Port' + str(port))
        s.bind((host,port))
        s.listen (5)
     
    except socket.error as msg:
        print ('Fehler beim Bind eines Sockets' + str (msg) + '/n' + 'neuer Verbindungsversuch..')
        bind_socket()

def socket_accept():
    conn, address = s.accept
    print ('Verbindung wurde aufgebaut unter  IP = ' + address[0] + ' Port' + str (address[1]))
    send_command(conn)
    conn.close()
#Senden von Befehlen an den Client
def send_command(conn):
    while True: #unendliche Schleife um das Schließen des Sockets zu verhindern
        cmd = input()
        if cmd == 'quit':
            conn.close()
            sys.exit()
        if (len(str.encode(cmd)) >0): #nur daten senden wenn Eingabe größer null)
            conn.send(str.encode(cmd))