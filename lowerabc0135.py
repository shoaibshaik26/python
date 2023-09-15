"""Write a program for revers of a charectors

A

B A

C B A

D C B A

E D C B A

F E D C B A

G F E D C B A

H G F E D C B A

I H G F E D C B A

J I H G F E D C B A

K J I H G F E D C B A

L K J I H G F E D C B A

M L K J I H G F E D C B A

N M L K J I H G F E D C B A

O N M L K J I H G F E D C B A
"""


import os 
import sys
os.system("cls")
for i in range(65,91):
    for z in range(i,64,-1):
        print(chr(z),end=" ")
    print("\n")   
    