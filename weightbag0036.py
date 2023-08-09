#write a function we to check the function is even or odd without the modules operator and logical bitwise

import os
import sys

BagWeight = int(input("please choose how you want to measure \n kilogram \n pounds "))
Kiloweight = float(input("please enter the weight : "))
  
if (BagWeight != 1):
    Kiloweight *= 0.4535923
if(Kiloweight > 23):
    print(" the weight of the bag is more than the required weight :%.2f" %(Kiloweight),"the pound value of excess is: %.2f"%(Kiloweight//0.45359230), end ='\n')
    print( " you have excess amount of weight: %.2f" %(Kiloweight-23), end = '\n')
else:
    print(" happy journy")