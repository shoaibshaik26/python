"""Write a Python program to find the intersection of two given arrays using Lambda.


array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
array_nums2 = [1, 2, 4, 8, 9]

"""

array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
array_nums2 = [1, 2, 4, 8, 9]

value = list(filter(lambda x : x in array_nums2,array_nums1))
#sector = value(array_nums1,array_nums2)
print(value)