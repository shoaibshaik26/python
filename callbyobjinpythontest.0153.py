# we are writing a program to do the loop for sum 
import os
os.system("cls")


def mytfunction():
    for i in range(valuestart,value+1): # value entering the negative value
        squre = i*i
        print(squre, end =", " if i < value else "\n") # this to remove the end comma in the value
    #print("%d"%(squre), end =", ") # this to remove the end comma in the value
        print( id(valuestart), id(value))
        print( hex(id(valuestart)), hex(id(value)),end ="\n\n")

valuestart= int(input("please enter a start range:"))
value = int(input("please set a end range:"))
print( id(valuestart), id(value),end ="\n")
print( hex(id(valuestart)), hex(id(value)),end ="\n\n")
sumoftotal = 0
mytfunction()