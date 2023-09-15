#printe a smile for a lower triangle in a matrix

import os 
import sys
os.system("cls")

name = int(input("how many set of lower triangle smiley you want"))



for i in range(0,name):
    for z in range(0,i+1):
        print(chr(1),end=" ")
    print("\n")   