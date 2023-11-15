#1. Write a Python program to triple all numbers in a given list of integers. Use Python map.


my_list = [1,2,3,4,5,6]

value = list(map(lambda my_list : (my_list ** 3),my_list))

print(value)

#2. Write a Python program to add three given lists using Python map and lambda.

my_list = [1,2,3,4,5,6]
my_list1 = [1,2,3,4,5,6]
my_list2 = [1,2,3,4,5,6]

value = list(map(lambda my_list,my_list1,my_list2 :(my_list+my_list1+my_list2),my_list,my_list1,my_list2))

print(value)


# Write a Python program to listify the list of given strings individually using Python map.

my_list = ["game","list","asdas"]

value = list(map(list,my_list))

print(value)


bases_num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(map(lambda bases_num, index :pow(bases_num, index),bases_num,index))
print(result)

#5. Write a Python program to square the elements of a list using the map() function.
my_list = [1,2,3,4,5,6]

value = list(map(lambda my_list : (my_list ** 2),my_list))
print(value)

#6. Write a Python program to convert all the characters into uppercase and lowercase 
#   and eliminate duplicate letters from a given sequence. Use the map() function.

my_list = ["game","list","asdas"]

value = list(map(lambda x : x.upper(), my_list))

print(value)



bases_num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(map(lambda bases_num, index :bases_num * index,bases_num,index))
print(result)
