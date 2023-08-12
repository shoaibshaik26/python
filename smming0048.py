# to join in swimming and atelatics 

import os
import sys

age = input("PLease enter age : ")

if(age.isalpha()):
    print("error")
else:
    age = int(age)
    if (age > 5):
        if age > 10:
            print("you are eligible for smming and atletic")
        else:
            print(" you can only swim")	
    else:
        print("not valid age")

