# write a programe that take only int else print error
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
try:
    number = int(input("please input the number where you want to end : "))
    NumberStart = int(input("please input the number where you want to start : "))
except ValueError:
        print("Invalid input. Please enter an integer.")
print("the sequence of number that are expected to be print %d to %d"%(NumberStart,number))
while(NumberStart <= number): # this is initialization and termination
		print( NumberStart, end=" ")
		#time.sleep(1)# time package to wait for some time 
		NumberStart = NumberStart + 1 #updation
else:
    print("the value is not valid")