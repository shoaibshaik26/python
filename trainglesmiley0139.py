# print a triangle of smiles 
import os 
import sys
os.system("cls")


rowofvalues  = int(input("no of rowsa please"))

for i in range(1,rowofvalues+1):
    rowofvalues = rowofvalues-1
    for item in range(rowofvalues,0,-1):
        print("",end=" ")
    for smiles in range(1,i+1):
        print(chr(1),end =" ")
    for values in range(1,i):
        print(chr(1),end=" ")
    print("")
    
    