#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 12:57:35 2022

@author: edyta
"""

import socket
from rich import print
import pickle 
import team_local_tactics
import mongoDB
import socket
import os
from _thread import *




#Server
ServerSideSocket = socket.socket()
host = socket.gethostname()
port = 8080 # initiate port no above 1024
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen(2)




out = []
returned = []
connections = []   



def new_game(connections):
    for conn in connections:
        conn.send(str(ThreadCount).encode())


        
def multi_threaded_client(connection):
    connection.send(str(ThreadCount).encode())
    
    while True:
        connections.append(connection)
        data = connection.recv(4096)
        message = pickle.loads(data)
        print(type(message))
        print(message)
        if not message:
            # if data is not received break
            break
        out.append(message[0])
        out.append(message[1])
        if len(out)==4:
            print("Client input ", out)
            returned = team_local_tactics.game(str(out[0]), str(out[1]),str(out[2]), str(out[3]))
            result = team_local_tactics.print_match_summary(returned)
            connections[0].send(result[0].encode())
            connections[1].send(result[0].encode())
            mongoDB.db(result[0],result[1], result[2], out)
            
            
            
            


while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
    if ThreadCount == 2:
        ThreadCount = 0

ServerSideSocket.close()


    
