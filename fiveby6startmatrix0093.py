#nested Loop 

#pritn a two dimensional matrix withe 5 row by 6 cloums matrix print * for every number 
""" nested loops can be implemented either using the for or while loops
	*A nested loops is the senario that will help in loop insted another loop
	*when the loops are implemented if the outer loop true and goes inside the inner loop until it is true it will not come out to the outer loop 
	*outer loop is paused until the inner loop is completed
	*loops can have else block as well
	"""
import os
import sys
os.system("cls")

valuerow = 1

while valuerow<5:
    valuecolumn=1
    while valuecolumn<=6:
        print("*", end= " ")
        valuecolumn+=1
    valuerow+=1
    print("\n")