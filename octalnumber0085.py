# print the OCtal number

#write a program for running total and moving average 
#python 3
# write a program for a factorial of a number
import os
import sys
import math
import time # time package
os.system("cls")
# we are going to start work with  while loop rember the below area before you write any thing
""" we have 5 basic components 
    1.initialization
    2.condition
    3.action
    4.updateion
    5.termination"""
number = int(input("Please enter the number"))
while number >0:
    print("squreroot of the number is",number,":", pow(number,2))
    print("cubethroot of the number is",number,":", pow(number,3))
    print("octal number  of the number is %d is %10o" %(number,number)) # octal number
    print(math.sqrt(number))
    number-=1
