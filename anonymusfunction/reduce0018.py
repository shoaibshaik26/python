# we are working with the reduce function in the functool module

# we are going to write the module with functool
import os
import functools 


bases_num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

result = functools.reduce(lambda bases_num, index :bases_num + index,bases_num)
print(result)

print("___________________error_________")
colors = [("red", 255, 0, 0), ("green", 0, 255, 0), ("blue", 0, 0, 255)]
result = functools.reduce(lambda bases_num, index :(bases_num +  index[1]),colors,0)

print(result)


print("_________reduce tupel list_________")



# bases_num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("give memory error")
# result = functools.reduce(lambda bases_num, index :(bases_num + index),bases_num,index)
# print(result)


print("_________reduce Max number_________")

lis = [1, 3, 5, 6, 2] 

result = functools.reduce(lambda lis,value : lis if lis > value else value,lis) 

print(result)
