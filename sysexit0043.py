#nestedIf 
#write aprogram postive and negative number"""
import os 
import sys

Number = float(input("Please enter the number : "))

if(Number == 0):
    print(" this neither postive or negative")    
	# we are only exit from the loop not the entire program.
    sys.exit()
    if(Number > 0):
        print("this is postive ")
else:
	print("negative")