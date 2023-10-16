# print factorial and each stage of factorial

# write a program for a power of number of a number
import os
import sys
import time # time package
os.system("cls")
# we are going to start work with  while loop rember the below area before you write any thing
import os
import sys
import time # time package
os.system("cls")
def power_recursive(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / power_recursive(base, -exponent)
    else:
        print(f"Calculating {base}^{exponent}")
        result = base * power_recursive(base, exponent - 1)
        print(f"{base}^{exponent} = {result}")
        return result

base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

result = power_recursive(base, exponent)
print(f"Result: {base}^{exponent} = {result}")