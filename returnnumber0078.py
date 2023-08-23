# priting a reverse number


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
innumber = reversenumber=returnreminder=originalnumber =0
innumber = int(input("please input the number  : "))
originalnumber = innumber

while( innumber != 0):
    returnreminder= innumber % 10
    print("returnreminder",returnreminder)
    print("reversenumber",reversenumber)
    reversenumber = int((reversenumber*10)+returnreminder)
    print("reversenumber",reversenumber)
    innumber = int(innumber/10)
    print(originalnumber,reversenumber)
    
    
