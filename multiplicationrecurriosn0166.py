"""What is recursion

A function that calls itself an argument is termed a recursion 



when the function is called it goes to the definition 

the control is passed to the function



operate on the definition and instruction and call the same function that is currently in operation(recursion)

the same function immediately executes goes to its definition completes its operation and returns to the calling function 

the stack is cleared only after the current called function is returned



Note: when the recursion is executed  if the proper care is not taken it can result in the deadlock 





when can we use recursion 

 any task that can do n to n-1 is highly suitable for the implementation 





a requirement like for recursion 



the problem is like n to n-1

recursive statement 

which can be a finite state 

What data structure is used while recursion is implemented 

recursion used internally stack structure as a data structure at Runtime

"""


import os
os.system("cls")


def mytfunction(valuestart,value):
	if valuestart>value:
		return 0 
	else:
		squre = valuestart * valuestart
		valuestart+=1
		increments = mytfunction(valuestart,value)
		print(squre)
		return increments


value = int(input("Please enter the value you want to end"))
valuestart = int(input("Please enter the value you want to start"))

cal= mytfunction(valuestart,value)
