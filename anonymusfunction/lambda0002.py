""" Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
Sample Output:
Double the number of 15 = 30
Triple the number of 15 = 45
Quadruple the number of 15 = 60
Quintuple the number 15 = 75"""
import os



def multi(value):
    valueaa =15
    return lambda value : valueaa * value

value = int(input("Please enter the number"))
result = multi(value)
result = result(value)
print(result)
