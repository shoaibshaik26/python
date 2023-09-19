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
			
			
"""
		whene functions have no parameters and there are no return value 
			we have to keep in mind that we need to design the all the fuction parameters and the parameters need to be designed all
			value in the fuction definations 
			variable
			expression 
			condition 
			iterations
			output
		the input data that has to be supplied to the function definition shoulf be plabbed when the calling to the function 
		same order as declared in the function adefination signature
		same number of arg in the function 
		the arg to the function call can be
			hard code value 
			soft code value 
			the name of the calling area in the function signature need not be same 
			"""

def addingtwonumber():

        value = int(input("Please enter the value "))
        value2 = int(input("Please enter the value2 "))
        sum = value+value2
        print(sum)
        return
    
    
def addingtwonumbers(value,value2): # the value and value2 are called formal parameters this is attaached when the function this is also called lazy bindings
    print(value+value2)
    