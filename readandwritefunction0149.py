def readname():
    firstname = input("firstname")
    middle = input("Middlename")
    lastname = input("lastname")
    writenames(firstname,middle,lastname)
    return

def writenames(firstname,middle,lastname):
    print(firstname,middle,lastname)

readname()

"""
        in the current context of the design the developer has
        designed the funcanility with 
        read operation module
        write operation module 
        as the the declared variable are local to the read variable
        added information to the write module as a passing information to the 
        write data function (passing the local variables as arguments
        which write data function carries the aruguments as paramets
        to the defination of the write data function and completes the requred operation
        
        """