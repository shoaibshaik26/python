#nestedIf 
#write a program accept char and vowel"""
import os 
import sys
print("please use lowercase only, uper case are not handled")
Number = input("Please enter the char : ")

if (Number == "a" ) or (Number ==  "e" ) or (Number == "i") or (Number == "o") or (Number == "u"):
    if Number == " ":
        print("This is none.")
    else:
        print("This is vowel.")
else:
    print("consonent.")