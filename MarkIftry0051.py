# check the marks for the class only with if TRY

import os
import sys
# this program will not work as it does not have the else block and only first if will excute
Marks =int(input("please input the marks"))
if((Marks > 0) and (Marks < 100)):
    if(Marks >= 86):
        print("this is grad A")
        if(Marks >= 61 and Marks <= 85):
            print( " the grade is B+")
            if (Marks >= 41 and Marks <= 60):
                print( " the grade is B")
                if(Marks >= 31 and Marks <= 40):
                    print( " the grade is C")
                else:
                    print("Failed")
else:
	print("The marks entired is not in range")