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
number = input("please input the number where you want to end : ")
NumberStart = input("please input the number where you want to start : ")
if(number == "" or NumberStart==""):
    print("you did not enter the number right")
    sys.exit()
else:
    number = int(number)
    NumberStart = int(NumberStart)
    if number<NumberStart:
        while number < NumberStart:
            print(number, end=" ")
            number = number + 1 #updation
    else:
        sumvalue = 0
        noofvalue = 1
        print("the sequence of number that are expected to be print %d to %d"%(NumberStart,number))
        while(NumberStart <= number): # this is initialization and termination
            noofvalue += 1
            print( NumberStart, end=" ")
            sumvalue = NumberStart + sumvalue
            Mean = sumvalue / noofvalue 
            NumberStart = NumberStart + 1 #updation
			
print("\n","the total for value is ",sumvalue)
print("the mean for the value is",Mean)
            