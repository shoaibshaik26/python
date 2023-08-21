#we are starting the while loop

# generate a sequece of number 1 to 5 

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
number = int(input("please input the number"))
NumberStart = 0
while(number > NumberStart): # this is initialization and termination
    print(number)
    time.sleep(1)# time package to wait for some time 
    number = number - 1 #updation