# using the zip function with the formates to display

# zip function accepts the iteratable object and make them concanitate in together

Itemsinbasket =["asdfas","asdfasd","asdf","asdf","asdf","sadf","asdf"]
itemsold=[1,12,121,12515,1561,1514,1454]

for items,item in zip(Itemsinbasket,itemsold):
	print(" we have product %s in the %d quantity" %(items,item))


# zip function accepts the iteratable object and make them concanitate in together

Itemsinbasket =["asdfas", "asdfasd","asdf","asdf","asdf","sadf","asdf"]
itemsold=[1,12,121,12515,1561,1514,1454]

ganble = zip(Itemsinbasket,itemsold)
print(set(ganble))
