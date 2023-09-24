import os
os.system("cls")

print(" we are writing a program to chek after adding a number in list does it change any thing in the address ")

print("________________collection_____________")


def collection(inalist):
    invalue = int(input("please let me know which value you want to change"))
    invalue2 = int(input("please let me know what value you want to update"))
    #inalist[invalue] = inalist.append(invalue2)
    #inalist[invalue] = inalist.insert(invalue,invalue2)
    inalist.insert(invalue,invalue2)
    print(inalist)
    print(inalist,hex(id(inalist)),id(inalist),end ="\n\n")


inalist=[1,2,3,4,5,6,7]
print(inalist,hex(id(inalist)),id(inalist),end ="\n\n")	
collection(inalist)
print(inalist,hex(id(inalist)),id(inalist),end ="\n\n")
print("________________see this gave the update value even this has been updated in the defination BUT ADDRESS REMAIN THE SAME _____________")	