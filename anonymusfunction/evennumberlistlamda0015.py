# filters in Lamda

"""
Function that need to be used in the lamdas

filter function in python 

filter acceptst a given sequence of the value supplied by collecions and filters the required  element given in the filter function 

the filter function internally applied an iterator upon the sequence of thr procress and apply for the each element in the procress

Sytaax is

Filter(condition, sequence)

"""
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [2,4,6,8]

value = list(filter(lambda list3: (list3 % 2 == 0),list1)) # here the list1 is acting as sending the list in the filter function.

print(value)