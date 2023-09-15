#printing a revers string using while loop
import os
os.system("cls")
value = input("please set a end range:")
value2 = len(value)
value1 = ""
while value2 >0:
    value1+=value[value2-1]# this is indexing pull up value
    value2-=1
print(value1)