# Write a programe to write a salarey of the employe based on the 1000 and more salarey

import os 
import sys

Name = input("please enter your Name")
salary = float(input("please enter the salary"))

if salary >=999:
    if (salary >=1000 and salary <=10000):
        print(" the house rent allowence is %s" %(Name), (salary*0.8)/100)
    else:    
        if (salary >=10001 and salary <=20000):
            print(" the house rent allowence is%s" %(Name), (salary*0.9)/100)
            print(" the dearness allowence is %s" %(Name), (salary*0.25)/100)
        else:
            if salary >=20001 and salary <=30000:
                print(" the house rent allowence is %s" %(Name), (salary*0.30)/100)
                print(" the dearness allowence is %s" %(Name), (salary*0.95)/100)
            else:
                if salary >=30001 and salary <=40000:
                    print(" the house rent allowence is ", (salary*1.25)/100)
                    print(" the dearness allowence is ", (salary*1.05)/100)
else:
    print("you will take full home salary :", salary)