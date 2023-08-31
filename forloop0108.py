# we are writing a program to do the loop for sum of 1+2+3+4+5
import os
os.system("cls")
valuestart= int(input("please enter a start range:"))
value = int(input("please set a end range:"))
sumoftotal = 0
for i in range(valuestart,value+1): # value entering the negative value 
	sumoftotal = sumoftotal + i
print(sumoftotal)