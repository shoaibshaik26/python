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


