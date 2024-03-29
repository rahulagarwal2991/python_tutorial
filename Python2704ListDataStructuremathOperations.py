
# ( + ) concatination operator
list1 =[1,2,3,4]
list2 =[5,6,7,8]
list = list1 + list2
print(list) #[1, 2, 3, 4, 5, 6, 7, 8]

# ( * ) Repetiation operator
list = [1,2,3,4]
list2 = list * 3
print(list2) # [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

# comparing of list objects  (==  !=)  Relational Operator(>, < , >= , <=) 
list1 =["a", "b", "c", "d"]
list2 =["a", "b", "c", "d"]
list3 =["A", "B", "C", "D"]

print(list1 == list2)
print(list1 != list2)
print(list1 == list3)

list1 =["a", "b", "c", "d"]
list2 =["a", "b", "d", "c"]
print(list1 > list2) #False
print(list1 < list2) #True
print(list1 <= list2) #True
print(list1 >= list2) #False

# Membership operators 
# 1. in operator
# 2. not in Operator

list =["a", "b", "c", "d"]
print("a" in list) #True
print("a" not in list) #False

# clear() function 
#This function is used to clear or remove all the data/elements from the list
list =["a", "b", "c", "d"]
print(list) #['a', 'b', 'c', 'd']
list.clear()
print(list) # []


# Nested list: A list inside a list is called as nested list
list =["a", "b", "c", "d", ["q", "w", "e", "r"] ]
print(list)

print(list[0]) # a
print(list[4][1]) # w

# nested list as matrix
# in python we can represent matrix using nexted list
nested_list = [ [1,2,3],[4,5,6],[7,8,9] ]
print(nested_list)

for i in range(0, len(nested_list),1):
    print(nested_list[i])

for i in range(len(nested_list)):
    for j in range (len(nested_list[i])):
        print(nested_list[i][j])

