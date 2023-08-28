#nested Loop 

#pritn a two dimensional matrix withe 12 by 12 matrix print * for every number 
""" nested loops can be implemented either using the for or while loops
	*A nested loops is the senario that will help in loop insted another loop
	*when the loops are implemented if the outer loop true and goes inside the inner loop until it is true it will not come out to the outer loop 
	*outer loop is paused until the inner loop is completed
	*loops can have else block as well
	"""
import os
import sys
os.system("cls")

valuerow1 =1

while valuerow1<=4:
    valuecolumn=1
    while valuecolumn<=4:
        print(" * ", end =" ")
        valuecolumn+=1
    valuerow1+=1
    print("\n")