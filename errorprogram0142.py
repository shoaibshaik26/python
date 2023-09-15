# function are nothing a set of instruction give to code 
# when the function is called the programe jumps to the function and continue the procress 

#error in the programe
triangle()# this will give the error ""name error"" the function is not defined.
import os 
import sys
os.system("cls")
print("error we have called the program before executation")

triangle()
def triangle():
    rowofvalues  = int(input("no of rowsa please"))

    for i in range(1,rowofvalues+1):
        rowofvalues = rowofvalues-1
        for item in range(rowofvalues,0,-1):
            print("",end=" ")
        for smiles in range(1,i+1):
            print(chr(1),end =" ")
        for values in range(1,i):
            print(chr(1),end=" ")
        print("")
    
    return



