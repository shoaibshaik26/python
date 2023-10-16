# print factorial and each stage of factorial

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
value1=factvalue = 1
for i in range( value1,number+1):
    value1 *= i
    print("%d "%(value1))
  
    