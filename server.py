#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 12:57:35 2022

@author: edyta
"""

import socket
from rich import print
import team_local_tactics
import mongoDB
from _thread import *
import time
import json


# Setup
ServerSideSocket = socket.socket()
host = socket.gethostname()
port = 8043 # initiate port no above 1024
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen(2) #Two clients


# Variables
ThreadCount = 0
out = []
returned = []
connections = []   
        
def multi_threaded_client(connection):
    connection.send(str(ThreadCount).encode())

    while True:
        connections.append(connection) #keep en eye on inncomming connections
        json_in = connection.recv(4096).decode() #str
        json_in_str = json.loads(json_in) #change to json
        out.append(json_in_str['P1'])
        out.append(json_in_str['P2'])
        
        if len(connections) >=2:
             send_to_client = json.dumps(json_in_str).encode()
             connections[1].send(send_to_client)
        
        if len(out)==4:
             returned = team_local_tactics.game(str(out[0]), str(out[1]),str(out[2]), str(out[3]))
             result = team_local_tactics.print_match_summary(returned)
             connections[0].send(result[0].encode())
             connections[1].send(result[0].encode())
             mongoDB.db(result[0],result[1], result[2], out)
             


# Multithread
while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))


    
