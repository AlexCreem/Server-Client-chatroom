# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 16:53:20 2019

@author: Mike Peterson, Alex Creem, Richard Colorusso
"""

import socket

print("This is the client for the multi threaded socket server!")
name = input("Enter your name: ")

s = socket.socket()
host=socket.gethostname()
port=8080

print(f"Connecting to server: {host} on port: {port}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
    try:
        sck.connect((host, port))
    except Exception as e:
        raise SystemExit(f"We have failed to connect to host: {host} on port: {port}, because: {e}")
        
##msg = input("What do we want to send to the server?: ")
    sck.send(name.encode())
    while True:
        msg = input("What do we want to send to the server?: ")
        ##sck.send(msg.encode())
        sck.sendall(msg.encode('utf-8'))
        if msg =='exit':
            print("Client is saying goodbye!")
            break
        data = sck.recv(1024)
        print(f"The server's response was: {data.decode()}")