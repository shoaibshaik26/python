# 

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
number = input("please input the number where you want to end : ")
NumberStart = input("please input the number where you want to start : ")
value = input("please input the o for odd and e for even : ")

if (value =="E" or value =="e"):
    number = int(number)
    NumberStart = int(NumberStart)
    while NumberStart < number:
        if(NumberStart % 2 == 0):
            print(NumberStart)
        NumberStart = NumberStart + 1 #updation
elif (value =="O" or value =="o"):
    number = int(number)
    NumberStart = int(NumberStart)
    while NumberStart < number:
        if(NumberStart % 2 != 0):
            print(NumberStart)
        NumberStart = NumberStart + 1 #updation
"""			
print("\n","the total for value is ",sumvalue)
print("the mean for the value is",Mean)"""