# Looping the data from the index 

startindex= endindex = 0
sumnumber = 0
startindex = int(input("enter the start range "))
endindex = int(input("enter the end range "))
for loop in range(startindex, endindex+1):
	sumnumber= sumnumber+loop
print("sum of vasle is %d"%(sumnumber))