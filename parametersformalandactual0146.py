#What are the types of parameters when designing a function .

#Formal parametres (lazay bingeders)

addingtwonumbers(value,value2): # the value and value2 are called formal parameters this is attaached when the function this is also called lazy bindings
    print(value+value2)

#actual parameters (the datatypes along with the actual values)



def addingtwonumber():

    value = int(input("Please enter the value "))
    value2 = int(input("Please enter the value2 "))
    sum = value+value2
    print(sum)
    return

addingtwonumber()# NO PARAMETS