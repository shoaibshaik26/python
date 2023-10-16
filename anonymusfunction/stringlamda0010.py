"""
Write a Python program to check whether a given string is a number or not using Lambda.
Sample Output:
True
True
False
True
False
True
Print checking numbers:
True
True

"""
value = '123456789'
print(value.isdigit())

valu1 = lambda value: value.isdigit()
print(valu1(value))
