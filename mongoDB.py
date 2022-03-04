#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 14:38:43 2022

@author: edyta
"""

from pymongo import MongoClient



def db(data, score1, score2, players):
    myclient = MongoClient("mongodb+srv://test:test@cluster0.yglec.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    mydb = myclient["mydatabase"]
    mycol = mydb["results"]
    mydict = {"Result": data, "Score Read Team": score1, "Score Blue Team": score2, "Players": str(players)}
    x = mycol.insert_one(mydict)
