import os
import sys
""" 
we are wrtring a program to use * args as it can accept n number of argements,

"""


def optionalvalue(*args):# args will take n argumets that at runtime without any trouble
    sumcalu =0
    for items in args:
        sumcalu+= items
    print(sumcalu)
    return 

def choice():
    choice = int(input("Please input the choice of operator"))
    return choice
def validation(choice):
	if choice ==1:
		operator =	int(input("Please enter the value to get sum"))
		optionalvalue(operator)
	elif choice ==2:
		operator =	int(input("Please enter the value to get sum"))
		operator1 =	int(input("Please enter the value to get sum"))
		optionalvalue(operator,operator1)
	elif choice ==3:
		operator =		int(input("Please enter the value to get sum"))
		operator1 =	int(input("Please enter the value to get sum"))
		operator3 =	int(input("Please enter the value to get sum"))
		optionalvalue(operator,operator1,operator3)

#choice()
val = choice()    
print("flag1")
validation(val)
print("flag2")
choiceinput = input("please let me know if you want to continue")

while choiceinput =="y":
    choice()
    validation(val)
    value2 = input("Please let me know if you want to stop")
    if value2 == "y":
        break
    else:
        continue