import os 
import sys
#we are here to check what are the bits that a variable is occuping

valueOfVariable = 'this how much'

print(sys.getsizeof(valueOfVariable),"bytes")


valueOfVariable = 'a'

print(sys.getsizeof(valueOfVariable),"bytes")