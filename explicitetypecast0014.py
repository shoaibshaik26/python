import os
import datetime

os.system("cls")

today = datetime.date.today()
year = today.year
age = input("Please enter your age, we will show the year you are born :")
explcitcast = int(age)
BirthYear = year-explcitcast
print(BirthYear)
