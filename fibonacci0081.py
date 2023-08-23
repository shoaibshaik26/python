# write a programe for a fibonacci series
# Illustrate the illiut 0,1,1,2,3,5
import os

starrange = 0 
fibinoci =1
while starrange<40:
    print(starrange)
    value1 = starrange+fibinoci
    starrange = fibinoci
    fibinoci = value1
    
    