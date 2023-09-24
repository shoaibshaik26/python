

# this program will help to show the scalar and the collection obj change in the phython 
def mytfunction(valuestart,value):
    """ this is Example program here we can see that we have changed the values in the end
        but while coming back to the outer level the value address will have the same value check out"""
    for i in range(valuestart,value+1): # value entering the negative value
        squre = i*i
        print(squre, end =", " if i < value else "\n") # this to remove the end comma in the value
        print("%d"%(squre), end =", ") # this to remove the end comma in the value
        print( id(valuestart), id(value))
        print( hex(id(valuestart)), hex(id(value)),end ="\n\n")
    print("The value of the address will be updated as the value below has been changed")
    print("_______changed___________")
    valuestart= 25
    value = 65
    print(valuestart, value, id(valuestart), id(value))
    print(valuestart, value, hex(id(valuestart)), hex(id(value)),end ="\n\n")	
    
    
if __name__ == "__main__":
    valuestart= int(input("please enter a start range:"))
    value = int(input("please set a end range:"))
    print( id(valuestart), id(value),end ="\n")
    print( hex(id(valuestart)), hex(id(value)),end ="\n\n")
    sumoftotal = 0
    print( valuestart, value, id(valuestart), id(value))
    print( valuestart, value, hex(id(valuestart)), hex(id(value)),end ="\n\n")
    mytfunction(valuestart,value)
    
    print( valuestart, value,id(valuestart), id(value))
    print( valuestart, value,hex(id(valuestart)), hex(id(value)),end ="\n\n")
	
	
	


print("________________collection_____________")


def collection(inalist):
    invalue = int(input("please let me know which value you want to change"))
    invalue2 = int(input("please let me know what value you want to update"))
    inalist[invalue]= invalue2
    print(inalist)
    print(inalist,hex(id(inalist)),id(inalist),end ="\n\n")


inalist=[1,2,3,4,5,6,7]
print(inalist,hex(id(inalist)),id(inalist),end ="\n\n")	
collection(inalist)
print(inalist,hex(id(inalist)),id(inalist),end ="\n\n")
print("________________see this gave the update value even this has been updated in the defination BUT ADDRESS REMAIN THE SAME _____________")	