

# Python Program to find palindromes in  
# a list of strings. 
  
my_list = ["geeks", "geeg", "keek", "practice", "aa"]
my_list2 = []
palindromes = list(filter(lambda my_list: my_list == "".join(reversed(my_list)),my_list))

print(palindromes)
