#If we want to execute a goup of statements multiple times then we use iterative stmts.
# for 
# while 

# for loop 
# If we want to execute some action for every element present in some sequence 

## Syntax
# for i in collection:
#     body

# where "range" is a collection
# i -> particular identifier

list =[1,2,3,4,5]
# print(type(list))
for i in list:
    print(i)
## output 
# 1
# 2
# 3
# 4
# 5


string_name = "geeks with geeks"
# print(type(list))
index = 0
for name in string_name:
    print("Index value  ", index , "present with ", name)
    index +=1

## output
# g
# e
# e
# k
# s
 
# w
# i
# t
# h
 
# g
# e
# e
# k
# s

## 
print("######")
value_set = [1,2,3,4,5]
for i in range(20,201,20):
    print(i)
print("######")
for i in range(1,11):
    print(13*i)