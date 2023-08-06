# python bin function to convert the decimal value to the binary value
# using replace we are replaceing the ob which is default to show the binaryvalue we are removing to notihing 


import os

value = int(input(" Please let me know the value for the binary"))
print( " this the binary value for the decimal number",value, bin(value).replace("0b","").zfill(10))