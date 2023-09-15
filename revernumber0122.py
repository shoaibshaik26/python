# printing the reverse of a number


startindex= endindex = 0
sumnumber = 0
startindex = input("enter the start range ")
for loop in range(len(startindex),0,-1):
    sumnumber=(startindex[loop - 1])
    print(sumnumber,end="")