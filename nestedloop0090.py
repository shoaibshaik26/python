#nested Loop 
""" nested loops can be implemented either using the for or while loops
	*A nested loops is the senario that will help in loop insted another loop
	*when the loops are implemented if the outer loop true and goes inside the inner loop until it is true it will not come out to the outer loop 
	*outer loop is paused until the inner loop is completed
	*loops can have else block as well
	"""
import os
import sys
os.system("cls")

loop = int(input("please enter the number of inner loop you want"))
oloop = int(input("please enter the number of inner oloop you want"))

while(loop >oloop):
    print(" this is outer1 loop")
    while (loop >oloop):
        print(" this inner loop")
        oloop+=1
    oloop+=1
else:
	print("this is outer2 loop")