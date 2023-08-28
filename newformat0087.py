# data formating usig string formating standards 
## New Formating

import os
import sys
import math
import time # time package
os.system("cls")

numbers = int(input("please input the number  : "))
value1= "asdfasdfa"
factvalue = 25
number = input("Please enter the string ")
print("octal number  of the number is {} ".format(number)) # new format
print("float number  of the number is %s " %(number)) # old format
print("octal number  of the number is {} ".format(number)) # new format
print("octal number %s of the number is  "%(number)) # old format
print("octal number {} of the number is  ".format(number)) # new format
print( "the value of the is ",numbers, value1,"with the age ",factvalue,number)
print( "the value of the is %d"%(numbers), "yhe string %s"%(value1),"with the age %0.2f"%(factvalue),number)
print( "the value of the is {}" "yhe string {}" "with the age ".format(numbers,value1,factvalue),number)
print( f"the value of the is {numbers}  yhe string {value1} with the age {factvalue}", number)# string interpolation
print( "the value of the is {1}" "yhe string {0}" "with the age ".format(numbers,value1,factvalue),number)


