# understanding the Logical flow of the functions and their calls

"""
the defination of the functions is never exposed Directely to the run-time enviroment 
the defination of the functions is loaded into the operation memory only when the functuion is called in the calleing env
 at run-time
when the program or the application in the execution state when the function is called it jupms to the function defination

all the operation statement exiting after the current call are suspended untill the function is returning from the defination

all the operation instruction is the defination of the function will take the priority immediately and the function actively operate in the memory 

onces all the operation within the function defination are completed the functions automaticaly returns to the calling env 
	when the function is returning to the calling function
		it return just ti the calling enviroment without the any value
		it may return to the calling enviroment without any values
		it may return to the calleing enviroment with a value
			note: the return statement at the end of the is not neccary when function is not returning any value 
			keep return the statement at the end of the function even the function is not return the value increases the readabilty  and clarity 
			there should be a return statement if return the value
				it is always return the only one datatype value(this is execption in python)
				once function def can contain multiple retuen statement but when execution in run-time finallu only one return statement will be actively involved
				the def of the function is said to be complete the moment the return statement is encounter
				""" 
import os
import time
import sys
os.system("cls")
print("we are starting here",end="\n\n")

# user def secetion start here

def integrationmodule():

	functiontwo()
	functionthree()
def functionone():
	""" we are starting the function 
	"""
	print(" this the first function")
	print("lets test this", end="\n\n")
	return
	
def functiontwo():
    """ we are starting the function"""
    functionone()
    # we are calling the function here in the this module will go to the function one
    #(this is called chaining function)
    print(" this the second function")
    print("lets test this", end="\n\n")
    return
def functionthree():
	""" we are starting the function 
	"""
	print(" this the three function")
	print("lets test this", end="\n\n")
	return
# user def end here 

#print("we are calling the function from the below we are going to the 27 line here returning from 32", end="\n")
#functionone()
#print("this out of loop", end="\n\n")
#time.sleep(3)

print("we are calling the function from the below externally", end="\n")
if __name__ == "__main__":
    integrationmodule()
    print("this out of loop", end="\n\n")
    print(integrationmodule.__code__.co_varnames)# this will tell the variables used in the run time 
time.sleep(3)

#print("we are calling the function from the below we are going to the 40 line here returning from 45", end="\n")
#functionthree()
#print("this out of loop")



