#Create a program that checks if a given number is even or odd and prints an appropriate message.

import os
import sys

Number = int(input("Please enter number"))

if (Number//2==0):
	print("the number is even ")
else:
	print("the number is odd")
	