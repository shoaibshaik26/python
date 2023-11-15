# the list of numeber which are deivisable by 13 my_list = [12, 65, 54, 39, 102,339, 221, 50, 70]
import os 
import functools


my_list = [12, 65, 54, 39, 102,339, 221, 50, 70]
def results(values):
    return values

def main(my_list):
    print("inside scope")
    result = list(filter(lambda my_list : (my_list % 13 == 0), my_list))
    print("out of the lamda")
    print("result of lambda",result)
    variables = results(result)
    return variables


print(main(my_list))
# co_consts will show the constant values in the code
# print(main.__code__.co_filename)# this will give you the filename of the code where it is been called
# print(results.__code__.consts)#constant will show the constant of the function
# print(results.__code__.name)#this will give the name of the file function in the code 
# print(results.__code__.covarnames)#this will give the variables passed in the function
# print(results.__code__.code)#this will give the byte code of the file
# print(main.__code__.co_argcount)#this will give the number of arguments passed
print(main.__code__.co_firstlineno)#this will give the number of arguments passed