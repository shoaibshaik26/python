#write a program for a loan 
#the program should calculate the amount for every year
#python 3
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

Pricipal = float(input("please enter finalcapitalamount"))
ROI= float(input("please enter ROI"))
numberofyear= float(input("please enter ROI"))

inyea = 0
while(inyea<numberofyear):
	Pricipal+= Pricipal*ROI/100.00
	inyea+=1
	print(numberofyear,Pricipal)
