import os
import sys
year = int(input(" please enter the year"))
if(year%4 == 0):
    if(year%100 == 0):
        if(year%400 == 0):
            print("this leapyear")
        else:
            print("this is not leap year")
    else:
        print("this is not leap year")
else:
    print(" this is not leap year")
