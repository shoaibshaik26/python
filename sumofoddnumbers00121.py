# Looping the data from the index 

startindex= endindex = 0
sumnumber = 0
startindex = 0
endindex = 10
for loop in range(startindex, endindex+1):
    if(loop %2 ==0):
        print("this is even number",loop)
    else:
        sumnumber= sumnumber+loop
        print("sum of vasle is %d"%(sumnumber))