import os
import sys
PersonName = input("Please enter the name ")
WeekDay = input( "Please enter the weekday")

if( (WeekDay == "sunday") or (WeekDay == "sunday") or (WeekDay == "monday") or (WeekDay == "Monday") or (WeekDay == "TUESDAY") or (WeekDay == "tuesday")):
    if((WeekDay == "Monday")or (WeekDay == "monday")):
        print("\n%s" %(PersonName),"you are born on Monday", end="\n")
    else:
        if((WeekDay == "Tuesday") or (WeekDay == "tuesday")):
            print("\n%s" %(PersonName),"you are born on Tuesday", end="\n")
        else:
            sys.exit

else:
	print("not valid")