# we are going to used the nested function call in the program

# any function that need to be used as a nested function call needs to have a return value



def optionalvalue(operator,optionalvalue):# args will take n argumets that at runtime without any trouble
    sumcalu = operator+optionalvalue
    print(sumcalu)
    return sumcalu
    

def choice():
    choice = int(input("Please input the choice of operator"))
    return choice
def validation(choice):
	if choice ==1:
		operator =	int(input("Please enter the value to get sum"))
		optionalvalue(operator)
	if choice ==2:
		operator =	int(input("Please enter the value to get sum"))
		operator1 =	int(input("Please enter the value to get sum"))
		optionalvalue(operator,operator1)
	if choice ==3:
		operator =	int(input("Please enter the value to get sum"))
		operator1 =	int(input("Please enter the value to get sum"))
		operator3 =	int(input("Please enter the value to get sum"))
		optionalvalue(operator,optionalvalue(operator1,operator3))# nested function call
#choice()
val = choice()    
print("flag1")
validation(val)
print("flag2")
choiceinput = input("please let me know if you want to continue")

while choiceinput =="y":
    val = choice()
    validation(val)
    value2 = input("Please let me know if you want to stop")
    if value2 == "y":
        break
    else:
        continue
    