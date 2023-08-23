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

number = int(input("please input the number  : "))
factvalue = 1
value1= number
if (number >2):
    while( number > factvalue):
        number-=1
        value1 *= number
    print(value1)
else:
    if(number>=1):
        print(number)
    else:
        print("do not enter negative value",number)