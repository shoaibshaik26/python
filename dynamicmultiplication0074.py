# write a multiple table upto defined range of user

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
number = int(input("please input the number  : "))
value = int(input("please input the number  : "))
value1 = 1
while(value1 <= value):
    print("%d *%02d= %02d"%(number, value1,(number * value1)))
    value1 += 1
