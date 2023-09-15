# write a programe to print following pattern

import os
os.system("cls")


for value in range(65,91):
    for items in range(value,64,-1):
        print(chr(items), end=" ")
    print()    
    