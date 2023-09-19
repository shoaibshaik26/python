# types of function as per the concept of accepting parameters and returning of value
"""
		functions that may or may not accept parameters
		function that may or may not have returning value 
	one function can accept zero or one ot more parameters by the nature of the procress for ehich is being developed
	depending the nature of the parameters that are passed as arguments and the returning type applied in returning statement
	the function cab be further  categorized into four types 
			
			
			
			functions that are not accepting any parameters and not returning any value
			function that are accepting parameters but not returning any value
			function not accepting any parameters but returning return value
			function that are accepting parameters and the return value
			
			"""
			
# write a program to accept two numbers

def addingtwonumber(value,value2):
    sum = value+value2
    print(sum)
    return
    
addingtwonumber(2,3) # sending paramets here 


value = int(input("Please enter the value "))
value2 = int(input("Please enter the value2 "))

def addingtwonumber(valu,values):
    sum = valu+values
    print(sum)
    return
addingtwonumber(value,value2)


def addingtwonumber():

    value = int(input("Please enter the value "))
    value2 = int(input("Please enter the value2 "))
    sum = value+value2
    print(sum)
    return

addingtwonumber()# NO PARAMETS 


def addingtwonumbers(value,value2):
    print(value+value2)
    
addingtwonumbers(2,3)