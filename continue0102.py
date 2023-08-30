
#illustrating continue staemenet in the program
#-----------------continue----------------------
import os
os.system('cls')

value1 = int(input(" please input a number to start"))
value2 = int(input("please enter a number to terminate"))
stopnumber = int(input("please enter a number to terminate abnormally"))
while value1<value2:
    if value1 == stopnumber:
        print("i have stop a  number", stopnumber, end =" ")
        value1+=1
        continue # this will only ignore the value 8 and continue for all other value
    else:
        print(value1, end=" ")
        value1+=1