# Please add sub mulitple and divide take input form user and show user the options for the operator

import os
import sys

Opertor = input("Please input the opertor")
Operator1 =int(input("Please enter number one"))
Operator2 =int(input("Please enter number one"))
if(Opertor == "+" or Opertor == "-" or Opertor == "*"):
    if(Opertor == "+"):
        print("the sum of the integere are ", Operator1 + Operator2)
    else:
        if(Opertor == "-"):
            print("the sub of the integere are ", Operator1 - Operator2)
        else:
            if(Opertor == "*"):
                print("the mul of the integere are ", Operator1*Operator2)
else:
    print("notvalid")