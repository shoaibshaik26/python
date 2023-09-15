#palendrom : both side the number will be same original number is the same as reverse number
# printing the reverse of a number

startindex = input("enter the start range ")
sumnumber =  ""
for loop in range(len(startindex),0,-1):
    sumnumber += startindex[loop - 1]    
if sumnumber == startindex:
    print(" this is a palendrom",startindex)
else:
    print(" this is not palendrom",sumnumber,end="")