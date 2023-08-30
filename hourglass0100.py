""" nested loops can be implemented either using the for or while loops
	*A nested loops is the senario that will help in loop insted another loop
	*when the loops are implemented if the outer loop true and goes inside the inner loop until it is true it will not come out to the outer loop 
	*outer loop is paused until the inner loop is completed
	*loops can have else block as well
	"""
import os
import sys
os.system("cls")

valueofrow = valueofcolumn = 0

nrowgeneration = int(input(""))

while valueofrow <= (nrowgeneration-1):
    valueofcolumn = 0
    while valueofcolumn<=valueofrow:
        print("", end= " ")
        valueofcolumn+=1
    print("")
    patternloop = valueofrow
    while patternloop < nrowgeneration:
        print("*", end = " ")
        patternloop+=1
    valueofrow+=1
    