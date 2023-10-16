# we are doing a keyword argument in the program 

#passing the values to the diffrent values


firstname = input("firstname")
middle = input("Middlename")
lastname = input("lastname")


def writename(firstname,middle, lastname):  # here we are interchanding the values to print the last name first
    print(lastname,middle,firstname)	
    #writenames()
    return
    
writename(lastname=lastname,middle=middle,firstname=firstname)
fullname = (firstname+middle+ lastname)
