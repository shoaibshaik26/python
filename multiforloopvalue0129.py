# for loop with multiple value and combaining with enum

# using the zip function with the formates to display

# zip function accepts the iteratable object and make them concanitate in together

Itemsinbasket =["asdfas","asdfasd","asdf","asdf","asdf","sadf","asdf"]
itemsold=[1,12,121,12515,1561,1514,1454]

for enum,(items,item) in enumerate(zip(Itemsinbasket,itemsold),1):
	print(" we have product %s in the %d quantity %d" %(items,item,enum))


# zip function accepts the iteratable object and make them concanitate in together

Itemsinbasket =["asdfas", "asdfasd","asdf","asdf","asdf","sadf","asdf"]
itemsold=[1,12,121,12515,1561,1514,1454]

ganble = zip(Itemsinbasket,itemsold)
print(set(ganble))
