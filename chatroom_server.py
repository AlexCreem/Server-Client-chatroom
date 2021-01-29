# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 15:40:26 2019

@author: Mike Peterson, Alex Creem, Richard Colorusso
"""

import socket
import threading

s = socket.socket()
host=socket.gethostname()
port=8080

print(f"Running the server on: {host} and port: {port}")
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
##connectionNumber = 0

try:
    s.bind((host, port))
    s.listen(10)    
except Exception as e:
    raise SystemExit(f"We could not bind the server on host: {host} to port: {port}, because: {e}")


def on_new_client(client, connection):
    ##connectionNumber = 0
    nameList = []
    ip = connection[0]
    port = connection[1]
    print(type(ip))
    name = client.recv(1024)
    print(f"THe new connection was made from IP: {name.decode()}, and port: {port}!")
    nameList.append(name.decode())
    ##connectionNumber += 1
    while True:
        msg = client.recv(1024)
        if msg.decode() == 'exit':
            break
        ##print(f"The client said:{ip} {msg.decode()}")
        print(f"{name.decode()}: {msg.decode()}")
        totalID = name.decode()+msg.decode()
        ##print(f"The client said: {msg.decode()}")
        reply = f"You told me: {msg.decode()}"
        client.sendall(reply.encode('utf-8'))
        for i in range(len(nameList)):
            if nameList[i] in totalID:
                print("FOUND THE IP")
                ##continue
            else:
                print ("WACK")
                client[i].send(msg.encode)
                
    print(f"The client from ip: {ip}, and port: {port}, has gracefully diconnected!")
    client.close()

while True:
    try:
        client, ip = s.accept()
        threading._start_new_thread(on_new_client,(client, ip))
    except KeyboardInterrupt:
        print(f"Gracefully shutting down the server!")
    except Exception as e:
        print(f"Well I did not anticipate this: {e}")

s.close()