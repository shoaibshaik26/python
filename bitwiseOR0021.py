#how the binary coversation is handelling in the python using OR
import os
os.system("cls")

value1 = 12
value2 = 26

print( " the value of 12 is",bin(12).zfill(8).replace("0b",""))
print( " the value of 26 is",bin(26).zfill(8).replace("0b",""))

result = value1 | value2

print( "if we are using the 'and' operator we see that there are many diffrence in the data int or any thing example 12 & 26  what we expect ?? i will leave it to you")
print(" this not because we have the diffrence 8 it is because it is converted in the bits and then the number we have received is  bitwise is this '1000' ")
print(bin(result).zfill(8))
print(int(bin(result)))

