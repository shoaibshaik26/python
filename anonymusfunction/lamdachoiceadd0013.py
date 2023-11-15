import os 




print("for pluse enter 1","\n")
print("for min enter 2","\n")
print("for mul enter 3","\n")

def valuecall(value):
    if value == 1:
        valueadd = lambda value1,value2 : value1+value2
        print("the sum of value is", valueadd(value1,value2)) 

value = int(input("Please enter your choice"))
value1 = int(input( " please enter number1"))
value2 = int(input( " please enter number2"))
valuecall(value)
