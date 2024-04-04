# Tuple Data Structure
# 1. immutable
# 2. Hatrogenous
# 3. () -> parenthesis and data seperatoed by comma
# 
td = ()
print(type(td)) #<class 'tuple'>
print(td) # ()

td = ()#valid
td = 1,2,3,4,5
td = 10
td = 10,
td = (10,)#valid
td = (10, 20, 30, 40, 50) #valid

list = [10,20, 30 ,40 ,50]
td = tuple(list)
print(type(td)) #<class 'tuple'>

# accessing data in tuple
td = (10, 20, 30, 40, 50)
print(td[1])
print(td[4]) # 50
print(td[-1]) # 50


# mathementical operations
td_1 = (10, 20, 30, 40, 50)
td_2 = (10, 20, 30, 40, 50)
td_3 = td_1 + td_2
print(td_3) #(10, 20, 30, 40, 50, 10, 20, 30, 40, 50)

# function
# 1. len()
# 2. count()
# 3. index()
# 4. sorted()
# 5. min() and max()



