#dynamic input of the name in lower triagle
#print using indexing 
"""
s

s h

s h a

s h a i

s h a i k
"""
import os 
import sys
os.system("cls")

name = input("please input your name")

lengthofname = len(name)

for i in range(0,lengthofname):
    for z in range(0,i+1):
        print(name[z],end=" ")
    print("\n")   