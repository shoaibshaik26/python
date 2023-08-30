#nested Loop 

"""pritn a two dimensional hower glass 
*****
****
***
**
*
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

valueofrow = 6
valueofcolumn = 1

while valueofrow >=0:
    valueofcolumn = 1
    while valueofcolumn<=6:
        print(" ",end=" ")
        valueofcolumn+=1
    print("\n")    
    patterncontrol = 1
    while patterncontrol <= valueofrow:
        print("*", end = " ")
        patterncontrol+=1
    valueofrow-=1
valueofrow = 1
valueofcolumn = 1

while valueofrow <=6:
    valueofcolumn = 1
    while valueofcolumn>=6:
        print(" ",end=" ")
        valueofcolumn+=1
    print("\n")    
    patterncontrol = 1
    while patterncontrol <= valueofrow:
        print("*", end = " ")
        patterncontrol+=1
    valueofrow+=1