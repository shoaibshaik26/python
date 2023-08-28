# write  program for the floating  hex and octa patern
## Formating

import os
import sys
import math
import time # time package
os.system("cls")

number = int(input("Please enter the number"))
while number >0:
    print("float number  of the number is %f is %10.2fo" %(number,number)) # octal number
    print("octal number  of the number is %d is %10o" %(number,number)) # octal number
    print("octal number  of the number is %d is %10o" %(number,number)) # octal number
    print("hex number  of the number is %d is %1x" %(number,number)) # hex number
    print("Hex number  of the number is %d is %010x" %(number,number)) # hex number
    print(math.sqrt(number))
    number-=1