
import os
os.system("cls")

Itemsinbasket = 5

for items in range(1,Itemsinbasket+1): #if we add one it will start from 1
    printvalue = 1
    for value in range(1,items+1):
        print(value, end= "")
        printvalue+=1
    print("\r")
    