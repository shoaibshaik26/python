




def readname():
    firstname = input("firstname")
    middle = input("Middlename")
    lastname = input("lastname")
    writenames(firstname,middle,lastname)
    return


def writenames(firstname,middle,lastname):
    print(firstname,middle,lastname)
    value2= input("do you want full name y or n ")
    if value2 == "Y" or value2 == "y":
        print( firstname+middle+lastname)
    else:
        print("thank you",firstname,lastname)


readname()