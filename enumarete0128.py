# atm machine with the access of enumarate function

"""
Enumerate function :

it can enumerate the data that are extracted from the collection.

it adds a counter to the iterable object and returns the object as an enumerating obj allocating one counter value for each element that is extracted.

It keeps the count of the loop

The returned enumerate obj can be used in loops to make the collection management easier

syntax is : 

enumerate(iterable-obj, start = 0)
"""

Itemsinbasket =["asdfas","asdfasd","asdf","asdf","asdf","sadf","asdf"]
itemsold=[1,12,121,12515,1561,1514,1454]

for items in enumerate(Itemsinbasket,1): #if we add one it will start from 1
#for items in enumerate(Itemsinbasket): 
	print(items)

"""
D:\python\script-intro>py enumarete0128.py
(1, 'asdfas')
(2, 'asdfasd')
(3, 'asdf')
(4, 'asdf')
(5, 'asdf')
(6, 'sadf')
(7, 'asdf')


output :
(0, 'asdfas')
(1, 'asdfasd')
(2, 'asdf')
(3, 'asdf')
(4, 'asdf')
(5, 'sadf')
(6, 'asdf')
"""