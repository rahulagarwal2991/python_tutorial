# Order of elements of list 
list = [10,20,30,40]
# to reverse the list we can use reverse() 
list.reverse()
print(list) #[40, 30, 20, 10]


# sort
list = [67,32,344,35,45,6,454]
# list.sort() 
print(list) #[6, 32, 35, 45, 67, 344, 454]
list.sort(reverse=True)
print(list) #[454, 344, 67, 45, 35, 32, 6]


# is , is not
# a = "Hello"
# b = "Hellos"
# print(a is not b)
# in , not in : value -> 1 , list -> [1,2,3,4]