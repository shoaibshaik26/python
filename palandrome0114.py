# write a program is palandrom or not

import os
os.system("cls")
value = input("please set a end range:")
value2 = len(value)
value1 = ""
while value2 >0:
    value1+=value[value2-1]# this is indexing pull up value
    value2-=1
if value == value2:
    print("this is a palandrom")
else:
    print("the reverse of the value is %s"%(value1))