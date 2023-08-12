# write a program for a validation before any person is registration for employment program 
 

import os

Age  = int(input(" please input what is your age "))
print("your age is : ", Age)

if (Age > 0 and Age <= 18 ):
    print( " the age is less than required age  :%0.2f" %(Age))
    print( "Pleease registed for employment scheam in gov")
else:
    print( "congratualition you can apply")