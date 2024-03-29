# List data Structure
# list = [1,2,3,4,5, "AC", 5]
# print(list)
# print(type(list))
s= "Python is a very good progamming lang"
list = s.split() #['Python', 'is', 'a', 'very', 'good', 'progamming', 'lang']
print(list)
print(type(list))

print(list[0]) #Python

list2 = list[0:4]
print(list2)

# Traversing elements of a list
# case 1 : by using while loop
list = [0,1,2,3,4,5,6,7,8,9]
i =0
while i < len(list):
    print(list[i])
    i = i+1
print("-----")
# case 2 : by using for loop
for l in list:
    print(l)
print("-----")

# case 3: to display only even numbers
for l in list:
    if l%2 == 0:
        print(l)
print("-----")

# case 3: to display only odd numbers
for l in list:
    if l%2 != 0:
        print(l)
print("-----")

# len() : to find the size of the list
list = [1,2,3,4,5]
length_of_list = len(list)
print(length_of_list) #5

# count() : to find the occurence of a value.
list = [1,1,2,3,3,3,3,3,3,4,5]

print(list.count(1)) #2
print(list.count(3)) #6

# index(): this is used to find the index of first occurence of the the item
list = [1,1,2,3,3,3,3,3,3,4,5]
print(list.index(1)) #0
print(list.index(3)) #3
