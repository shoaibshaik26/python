'''What are mandatpry arguments in python 
	mandatory arguemtns in python refer to such argumets  or parameters that need to be definitely supplied at the time of calling 
	if you have declared a function and kept a parameters then the concept of the arugemt madatory arise or optional argements 
	 '''
	 
# we are working on the parameters that are mandatory and optional parameters

import os
os.system("cls")

print(" we are writing a program to for actual and mandatory parameters ")

print("________________sum and calling_____________")

def mytfunction(valuestart,value):
    for i in range(valuestart,value+1): # value entering the negative value
        squre = i*i
        print(squre, end =", " if i < value else "\n") # this to remove the end comma in the value
    #print("%d"%(squre), end =", ") # this to remove the end comma in the value

valuestart= int(input("please enter a start range:"))
value = int(input("please set a end range:"))
value2 = int(input("please set a end range:"))
sumoftotal = 0
mytfunction(valuestart,value,value2)# calling with three parameters
#OUTPUT
#OUTPUT
#OUTPUT
#OUTPUT
# TypeError: mytfunction() takes 2 positional arguments but 3 were given