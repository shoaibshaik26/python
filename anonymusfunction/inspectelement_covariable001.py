# the list of numeber which are deivisable by 13 my_list = [12, 65, 54, 39, 102,339, 221, 50, 70]
import os 
import functools


my_list = [12, 65, 54, 39, 102,339, 221, 50, 70]
def main(my_list):
    result = list(filter(lambda my_list : (my_list % 13 == 0), my_list))
    return result

print(main(my_list))

print(main.__code__.co_varnames)