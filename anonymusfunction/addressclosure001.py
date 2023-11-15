# the list of numeber which are deivisable by 13 my_list = [12, 65, 54, 39, 102,339, 221, 50, 70]

# working with the closure and address of the variable
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

main
print("this the address ",main)
value = main
print("this the value ",value)