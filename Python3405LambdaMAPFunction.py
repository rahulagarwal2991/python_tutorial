# WAP to find squre of give numbers using lambda and map function

list1 = [1,2,3,4,5]
list_data = map(lambda x : x*x, list1)
list_data = list(list_data)
print(list_data) # [1, 4, 9, 16, 25]