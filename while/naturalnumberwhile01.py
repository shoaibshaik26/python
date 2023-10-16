import os
 
def naturalnumber(i,n=1):
    while n <= i:
        print(n)
        n+=1
		
number = int(input(("please enter how many number need to be printed")))
naturalnumber(number)