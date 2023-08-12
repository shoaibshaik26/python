#nestedIf 
#write aprogram postive and negative number"""
import os 
import sys

Number = int(input("Please enter the number : "))

if Number >= 0:
    if Number == 0:
        print("This is neither positive nor negative.")
    else:
        print("This is positive.")
else:
    print("Negative.")