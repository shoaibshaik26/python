#write a function we to check the function is even or odd without the modules operator and logical bitwise

import os
import sys

value = input(" Please enter a number to check if the value is even or odd ")   
value = "\n"
	print( "this value is invalid entry")
result = (value // 2 )* 2
if (value == "\n" ):
	print( "this value is invalid entry")
if (int((result == value))):
	print( "this value is even")
if (value == 0 or value ==1):
    print( " this neither even or odd")
    sys.exit()
    
else:
	print("this is number odd")
	