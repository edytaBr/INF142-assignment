#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 12:57:34 2022

@author: edyta
"""

import socket
import pickle 
from rich import print
import team_local_tactics


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 7026  # socket server port number
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    send_package = ""
    game = []
    while send_package.lower().strip() != 'n':
        num = client_socket.recv(4096).decode()
        team_local_tactics.clientSiteGame()
        game = (team_local_tactics.clientSiteGame2(num, game))
        print("length", len(game))
        send_package = pickle.dumps(game)
        client_socket.send(send_package)
                
        data = client_socket.recv(4096).decode()  # receive response
        print('Received from server: ' + data)  # show in terminal
        send_package = input("Do you want to play again, Y/N ")
        client_socket.send(str(send_package).encode())

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()