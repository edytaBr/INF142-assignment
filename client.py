#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 12:57:34 2022

@author: edyta
"""

import socket
from rich import print
import team_local_tactics
import json


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 8082  # socket server port number
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    send_package = ""
    game = []
    while send_package.lower().strip() != 'n':
        num = client_socket.recv(1024).decode()
        
        if num == "1":
            team_local_tactics.clientSiteGame()
            game = (team_local_tactics.clientSiteGame2("1", game))
            
            jsonResult = {"P1":game[0], "P2":game[1]}
            jsonResult = json.dumps(jsonResult).encode()
            client_socket.send(jsonResult)

        elif num == "2":
            team_local_tactics.clientSiteGame()
            print("Waiting for player 1 to send input")
            j1 = client_socket.recv(1024).decode()
            print("Json received -->", j1)
            s1 = json.loads(j1)
            
            
            # Get Player 1 input to compare rep
            enemies = []
            enemies.append(s1['P1'])
            enemies.append(s1['P2'])

            game = (team_local_tactics.clientSiteGame2("2", enemies))
            jsonResult2 = {"P1":game[0], "P2":game[1]}

            jsonResult2 = json.dumps(jsonResult2).encode()
            client_socket.send(jsonResult2)
            sendt = client_socket.recv(1024).decode()  # receive response
            
        result = client_socket.recv(1024).decode()  # receive response
        print('Received from server-match result: ' + result)  # show in terminal
       
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()