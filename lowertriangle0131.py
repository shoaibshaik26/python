# write a programe to print the lower triangle with charestors
import os
os.system("cls")

value = 5
for value in range(65,91):
    value2= 65
    for items in range(65,value+1):
        print(chr(items), end=" ")
    print()    