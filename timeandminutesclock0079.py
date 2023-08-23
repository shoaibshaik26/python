# write a program to simulate a digital clock  with a limitation of 24 hours 

#python 3
# write a program for a factorial of a number
import os
import sys
import time # time package
os.system("cls")
# we are going to start work with  while loop rember the below area before you write any thing
""" we have 5 basic components 
    1.initialization
    2.condition
    3.action
    4.updateion
    5.termination"""
Hours = minutes = seconds =0 

while True:
    seconds+=1
    if(seconds == 60):
        seconds = 0
        minutes += 1
    if(minutes == 60):
        Hours += 1
        minutes = 0
        seconds = 0
    if(Hours == 24):
        Hours = 0
        minutes = 0
        seconds = 0
    print(seconds,minutes,Hours)