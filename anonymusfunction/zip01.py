keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = zip(keys,values)

print(list((result)))
#we are using the zip function to combine two list in one 


dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

result2 = {**dict1,**dict2}
print(result2)