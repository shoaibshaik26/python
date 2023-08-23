# write a multiple table upto 10

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
number = int(input("please input the number where you want to end : "))
value = 1
while(number <= 10 and value <= 10):
    print("%d *%02d= %02d"%(number, value,(number * value)))
    value += 1
