# write a program to print rever of the number given as a string

""" 
-------------for loop --------------

For loops

when we use for loop it is a dynamic loop 

mostly for loop operates on range evalutuion of the data

when range is iteratable with indexing

every for loop has at least one indexing which is auto declaed and managed as the loop in advancing

 for loop contain in keyword which actulally identifies the objects on ehich the iteration has been oimplemented 
sytanx:

For <index variable> in <sequence>

What is the most used keyword in for loop 

it is Range 

how many aurguments we can take

we can have (range start, range end, incremental value)

can we have else block in for

we can have else in for as well

we can use range for both postive and negative value 
"""


# we are writing a program to do the loop for sum 
import os
os.system("cls")
value = input("please set a end range:")
valueinicial = ""
for i in range(len(value),0,-1): # value entering the negative value
    valueinicial += value[i-1]
print(valueinicial,end="")