# unpacking the data in the for loop is simple in the set by the adding set of multiple variable in the loop.

Itemsinbasket =["asdfas","asdfasd","asdf","asdf","asdf","sadf","asdf"]
itemsold=[1,12,121,12515,1561,1514,1454]

for item, items in zip(Itemsinbasket,itemsold):
	print(item,items)

