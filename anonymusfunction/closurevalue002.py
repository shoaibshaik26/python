# the list of numeber which are deivisable by 13 my_list = [12, 65, 54, 39, 102,339, 221, 50, 70]

# working with the closure and address of the variable
import os 
import functools


my_list = [12, 65, 54, 39, 102,339, 221, 50, 70]
def results():
    print("I am in the outer scope")
    def main(my_list):
        print("inside scope")
        result = list(filter(lambda my_list : (my_list % 13 == 0), my_list))
        print("out of the lamda")
        print("result of lambda",result)
        return result
    return main



print(results())
print("______________calling the outer function_______")
# print(results())#printing from the direct funcational call
valuefromain = results()
print(valuefromain(my_list))# printong from indirect funcational call 
print("______________calling the inner function_______")