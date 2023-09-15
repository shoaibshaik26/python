# defining a function

"""A function is a process that converts the one value to another value is called function

every function has two fundamental components

the set of allowed input to the function is called as domain of the function 

the set of possible output returned by the operation of the function called the range of the function

function allow the programer to write down the program into subtask and make the over problem easy.

it makes one step call after another step.

it allow to have the namespace clean and readable creating a concept of memory localization promising a consistent and situational use of the memory space

function helps with the memory localization

it makes testing modular easier 

it contains parameters and arguments.

"""
import os 
import sys
os.system("cls")

def triangle():
    rowofvalues  = int(input("no of rowsa please"))

    for i in range(1,rowofvalues+1):
        rowofvalues = rowofvalues-1
        for item in range(rowofvalues,0,-1):
            print("",end=" ")
        for smiles in range(1,i+1):
            print(chr(1),end =" ")
        for values in range(1,i):
            print(chr(1),end=" ")
        print("")
    
    return


triangle()


def sixbysix():
    name = int(input("how many set of lower triangle smiley you want"))
    for i in range(0,name):
        for z in range(0,name):
            print(chr(1),end=" ")
        print("\n")
    return
sixbysix()
# calling the function for the abtract of the usage 
# the excusation start from the 44 line and the program immediately 
#suspends all the next level of the activities  and jumps to the location where the call to the function
#