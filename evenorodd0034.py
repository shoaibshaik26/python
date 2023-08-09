# we are going to write a programe to check even or odd using a if and else statement

import os
import sys

value = int(input(" Please enter a number to check if the value is even or odd "))

if ((value & 1)==0):
	print( "this value is even")
if (value == 0 or value ==1):
    print( " this neither even or odd")
    sys.exit()
else:
	print("this is number odd")
	