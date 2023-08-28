# write  program for the floating  hex and octa patern
## Formating


#Working with postional parameters
#-------------O--------------------------
import os
import sys
import math
import time # time package
os.system("cls")

number = int(input("Please enter the number"))
numbers = input("please input string")
value1 = "aasdfasdfasdf"
while number >0:
    print("float number  of the number is %f is %10.2fo" %(number,number)) # octal number
    print("octal number  of the number is %d is %10o" %(number,number)) # octal number
    print("octal number  of the number is %d is %10o" %(number,number)) # octal number
    print("hex number  of the number is %d is %1x" %(number,number)) # hex number
    print("Hex number  of the number is %d is %010x" %(number,number)) # hex number
    print(math.sqrt(number))
    number-=1
	
	#Working with postional parameters
#-------------O--------------------------

print( "the value of the is {1}" "yhe string {0}" "with the age ".format(numbers,value1,),number)
print( "the value of the is {1:>155}" "yhe string {0}" "with the age ".format(numbers,value1,),number)# right aligement
print( "the value of the is {1:<155}" "yhe string {0}" "with the age ".format(numbers,value1,),number)# left alignment
print( "the value of the is {1:^155}" "yhe string {0}" "with the age ".format(numbers,value1,),number)# center alignment
print( "the value of the is {0:_^155}" "yhe string {1}" "with the age ".format(numbers,value1,),number)# adding the padding charectors 