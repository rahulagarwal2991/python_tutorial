# list = []
# i = 0
# while i == 0:  
#     data = int(input("enter the data or press 0 to exit"))
#     if(data == 0):
#         i =1
#     else:
#         list.append(data)

# print(list)

# Manipuation of a list
# append()
# insert()
# extend()
# remove()
# pop()

# append() : this is used to add an exta item in the list
list = []
list = [89,65,645,4,534,34,43,43,45]
list.append(1)
list.append(2)
list.append(3)

print(list) #[89, 65, 645, 4, 534, 34, 43, 43, 45, 1, 2, 3]


# insert() : inset is used to insert the data at a particular index
list.insert(3, 1000)
print(list) #[89, 65, 645, 1000, 4, 534, 34, 43, 43, 45, 1, 2, 3]

# if the specified index is greater than max index then element 
# will be inserted in the last position.

list.insert(30, 1000)
print(list) #[89, 65, 645, 1000, 4, 534, 34, 43, 43, 45, 1, 2, 3, 1000]

# if the specified index is smaller than min index then the value will be added at first position
list.insert(-30, 1000)
print(list)

# extend() 
list1= ["a","b","c"]
list2 = [1,2,3]
list1.extend(list2) # list1 will have all data of list2
print(list1) #['a', 'b', 'c', 1, 2, 3]


list2.extend(list1) # list2 will have all data of list1
print(list2) #[1, 2, 3, 'a', 'b', 'c', 1, 2, 3]

# remove() this function is used to remove a particular value from the list
list= ["a","b","c"]
list.remove("c")
print(list)
####
list= ["a","b","c"]
list =[]
### 
# pop() : it removes the list element from the list
list= ["a","b","c"]
print(list.pop())
print(list)

list.pop()
print(list)

list.pop()
print(list)

