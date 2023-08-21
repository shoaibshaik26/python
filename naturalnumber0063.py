# write a programe to print the natural number

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
number = int(input("please input the number till which you want to print : "))
NumberStart = 1
print("the sequence of number that are expected to be print %d to %d"%(NumberStart,number))
while(NumberStart <= number): # this is initialization and termination
		print( NumberStart, end=" ")
		#time.sleep(1)# time package to wait for some time 
		NumberStart = NumberStart + 1 #updation