# and or not -> True or False
# and -> in c &&
# or  -> in c ||
# not -> in c !
#we can apply these logical operators on all data types

# for Boolean Data type
# and -> if all values are true then only it will give true
# or -> if any of the value is true then output will be true
# not -> opposite output
 
# and
print(True and True) # True 1*1 = 1 True
print(True and False) # False 1*0 = 0 False
print(True and True and True) # True
print(True and True and False) # False

# or
print(True or True) # True 1+1 = 2 True
print(True or False) # False 1+0 = 1 True
print(True or True or True) # True
print(True or True or False) # True
print(False or False or False) # 0+0+0 => 0 False

# not
print(not True) #False
print(not False) # True

# With Non boolean type
# 0 means False
# Any value greater than 0 -> True
# "" -> False

#x and y
print(10 and 20) # 20
print(0 and 20)  # 0

#x or y
print(10 or 20) # 10
print(0 or 20)  # 20

#not x
print(not 10) # False
print(not 0) # True