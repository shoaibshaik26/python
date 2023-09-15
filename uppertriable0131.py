# write a programe to print the lower triangle with charestors
import os
os.system("cls")

value = 5
for value in range(91,65,-1):
    value2= 91
    for items in range(65,value-1):
        print(chr(items), end=" ")
    print()    
    
    
    """ A B C D E F G H I J K L M N O P Q R S T U V W X Y
A B C D E F G H I J K L M N O P Q R S T U V W X
A B C D E F G H I J K L M N O P Q R S T U V W
A B C D E F G H I J K L M N O P Q R S T U V
A B C D E F G H I J K L M N O P Q R S T U
A B C D E F G H I J K L M N O P Q R S T
A B C D E F G H I J K L M N O P Q R S
A B C D E F G H I J K L M N O P Q R
A B C D E F G H I J K L M N O P Q
A B C D E F G H I J K L M N O P
A B C D E F G H I J K L M N O
A B C D E F G H I J K L M N
A B C D E F G H I J K L M
A B C D E F G H I J K L
A B C D E F G H I J K
A B C D E F G H I J
A B C D E F G H I
A B C D E F G H
A B C D E F G
A B C D E F
A B C D E
A B C D
A B C
A B
A
"""