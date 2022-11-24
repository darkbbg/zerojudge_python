# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 21:52:19 2022

@author: BUQhomeNB
"""

yy=[] #list

while True:
    strr=input()
    
    if strr=="EOF":
        break
    
    #yy.append(int(strr))
    
    if(int(strr)%400==0):
        yy.append("閏年")
    else:
        yy.append("平年")

for i in yy:
    print(i)