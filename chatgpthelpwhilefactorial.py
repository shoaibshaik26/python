import os

# Input a number for which you want to calculate the factorial
num = int(input("Enter a number: "))

# Initialize variables
factorial = 1
i = 1

# Initialize a string to store the factorial expression
factorial_expression = ""

# Calculate factorial using a while loop and build the expression
while i <= num:
    if i > 1:
        factorial_expression += "*"
    factorial_expression += str(i)
    factorial *= i
    i += 1

# Print the factorial expression
print(factorial_expression)
