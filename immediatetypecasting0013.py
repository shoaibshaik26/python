#Immediate type casting 
""" here we are coverting the data at the run time"""
import os
import datetime

os.system("cls")

today = datetime.date.today()
year = today.year
age = int(input("Please enter your age, we will show the year you are born :"))
BirthYear = year-age
print(BirthYear)




