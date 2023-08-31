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
import os
os.system("cls")
value = int(input("please set a range value :"))

for i in range(value+1):
	print(i)
else:
    if value >i:
        print("error")
