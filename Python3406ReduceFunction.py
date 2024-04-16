# Reduce() Function:

# syntax :
# reduce(function, sequence)

# functools

from functools import *

list1 =[10,20,30,40,50]

result = reduce(lambda x,y : x+y, list1)

print(list(result)) # 150