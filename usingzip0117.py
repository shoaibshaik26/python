# we are writing a program to use zip function 
"""
	there are two values in the zip function we have containers and iteratable \
	
	
	
	"""
import os 
import sys
os.system("cls")

arraylist = [1,2,3,4,5,6,7]
arrays = ["sho","asda","asdasd","weqweqwe"]

for number,values in zip(arraylist,arrays): # this will print values as a list of elements
	print("%d this is the value of the two elements %s"%(number,values))
	