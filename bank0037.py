# write a program for a bank transaction and cash withdraw 

import os

Transaction  = int(input(" please input what you want to do \n 1. cash withdrawal \n 2.deposit"))
amount = int(input( "Please enter the amount :"))

MinimumBalance = 5000
currentBalance = 25000
if (Transaction != 1):
    currentBalance += amount
    print( " the amount has been deposit :%0.2f" %(currentBalance))
else:
    if(currentBalance < amount):
        print(" your balance is less than the minimum amount sry")
    else:
        currentBalance -= amount
        print( " the amount balance is :%0.2f" %(currentBalance))
