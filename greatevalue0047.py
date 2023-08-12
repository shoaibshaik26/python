# greates of the three number, commonsense base validations
import os
import sys
Value1 = input("number1 ")
Value2 = input("number2 ")
Value3 = input("number3 ")

if((Value1 == Value2) or (Value1 == Value3) or (Value2 == Value3) ):
        print(" Please  do not enter duplicate value")
if((Value1.isalpha()) or (Value2.isalpha()) or (Value3.isalpha())):
    print("not valid")
else:
    if(Value1  > Value2 ):
        if(Value1  > Value3 ):
            print("value1 is greater")
        else:
            print("value3 is greater")
    else:    
        if(Value2 >Value3):
            print("value2 is greater")
        else:
            print("value 3 is grater")
    
    