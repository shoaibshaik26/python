# print factorial and each stage of factorial

# write a program for a power of number of a number
import os
import sys
import time # time package
os.system("cls")
# we are going to start work with  while loop rember the below area before you write any thing
import os
import sys
import time # time package
os.system("cls")
def squreloopp(number,value):
    original = number
    for i in range(0,value):
        number *= original
        #print("%d "%(number))
    return number
        
        
number = int(input("please input the number  : "))    
value = int(input("please input the power number  : "))    
values = squreloopp(number,value)
print(values)