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
def factorial(number, value1,factvalue):
    if factvalue>value1:
        return 0
    else:
        number = number *factvalue
        factvalue+=1
        #print(number,value1,factvalue)
        value = factorial(number,value1,factvalue)
        print("falg",number)
  
number = int(input("please input the number  : "))
value1= int(input("please input the number  : "))
factvalue = 1    
valuese = factorial(number,value1,factvalue)
#print("here",valuese)