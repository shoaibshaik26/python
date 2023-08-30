#nested Loop 

"""pritn a two dimensional matrix withe1*2 matrix print * for every number 
1
1 2
1 2 3
1 2 3 4
"""

""" nested loops can be implemented either using the for or while loops
	*A nested loops is the senario that will help in loop insted another loop
	*when the loops are implemented if the outer loop true and goes inside the inner loop until it is true it will not come out to the outer loop 
	*outer loop is paused until the inner loop is completed
	*loops can have else block as well
	"""
import os
import sys
os.system("cls")

valuerow = valuecolumn= 1

while valuerow<=5:  #row controler
    valuecolumn = 1
    while valuecolumn<=valuerow: # colum controler
        print("%d" %(valuecolumn),end=" ")
        valuecolumn+=1
    print(end="\n")
    valuerow+=1