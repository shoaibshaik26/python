# we are workig on the optional arguments

# we are working on the parameters that are mandatory and optional parameters
""" optional parameters are also called default parameters and when we declared the defination of the function for accepting the paramertes
        when the function has default paramertes the end user while calling the function need not supply the value  to default arguments 
                if the default argumets are not supplied the interpetor will continue with the values that are defined at the time  of
                design  fulfilling the function with all the paramertes
"""

import os
os.system("cls")

print(" we are writing a program to for actual and mandatory parameters ")

print("________________sum and calling_____________")

def mytfunction(valuestart,value=8):# here we are defaulting the value to zero, we are making this as a optional parameter
    for i in range(valuestart,value+1): # value entering the negative value
        squre = i*i
        print(squre, end =", " if i < value else "\n") # this to remove the end comma in the value
    #print("%d"%(squre), end =", ") # this to remove the end comma in the value


# def valueinput():

    # sumoftotal = 0
    # return valuestart,value
def valuecheck(valuestart,value):
   # valueinput()
    if value !=0 and valuestart !=0:
        mytfunction(valuestart,value)
    else:
        if value ==0 and valuestart ==0:
            print("both the value are zero")
        else:
            if value ==0: 
                mytfunction(valuestart)
def valueinput1():  
    valuestart= int(input("please enter a start range:"))
    value = int(input("please set a end range:"))
    valuecheck(valuestart,value)

valueinput1()
#OUTPUT
#OUTPUT
#OUTPUT
#OUTPUT
# TypeError: mytfunction() takes 2 positional arguments but 3 were given