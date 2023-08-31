# write a program to print squres of the number

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
valuestart= int(input("please enter a start range:"))
value = int(input("please set a end range:"))
sumoftotal = 0
for i in range(valuestart,value+1): # value entering the negative value
    squre = i*i
    print(squre, end =", " if i < value else "\n") # this to remove the end comma in the value
    #print("%d"%(squre), end =", ") # this to remove the end comma in the value