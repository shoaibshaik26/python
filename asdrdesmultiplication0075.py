# print the table in asd and desc

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
order = input("do you want in asd or desc only A and D :")
value1 = 1
if (order == "A" or order =="a"):
    while(value1 <= value):
        print("%d *%02d= %02d"%(number, value1,(number * value1)))
        value1 += 1
else:
    if (order == "D" or order == "d"):
        while(value > 0):
            print("%d *%02d= %02d"%(number, value,(number * value)))
            value -= 1