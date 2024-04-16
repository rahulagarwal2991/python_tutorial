# use of map function and min , max 
list1 = [12, 45, 33, 22]
print(min(list1))
print(max(list1))

# # map(function_name, list)
list1 = [12, 45, 33, 22]
def double(x):
    y = 2*x
    return y

output = map(double, list1)
output_list = list(output)
print(output_list)

#######
# list_set = input("enter the list").split() # ['1', '2', '3', '4', '5', '6', '7', '8', '9']

list_set = map(int, input("enter the list").split())
list_set = list(list_set)

print(list_set) # [1, 2, 3, 4, 5]