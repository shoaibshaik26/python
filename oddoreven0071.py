# print handle the value that handles the empty statements and handle lower to higher value
# add numbers as well and print sum of the values.
# handeling Mean

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
value = int(input("Please enter int input to check odd or even "))

if (value %2 ==0):
	print(" this is even")
else:
	print("this is odd")