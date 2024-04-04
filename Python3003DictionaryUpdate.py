# update a dictionary data
# to update any dictionary data we need to pick the key and then we can update the value part.
dict_students_data = {
    "ram"  : 90,
    "shyam": 91,
    "sita" : 92,
    "geeta": 93,
}
print("Before Change: ")
print(dict_students_data)
dict_students_data["ram"] = 95 # this will replace old value with new value.

# if the key we seelected is not available the a new entry gets created.
print("After Change: ")
print(dict_students_data)


# clear(): This is used to remove all enteries from the directory
dict_students_data.clear()
print("After clear method: ")
print(dict_students_data) #{}

# del keyword: This is used to delete a dictionary
del dict_students_data

print("After Del keyword: ")
# print(dict_students_data) # NameError: name 'dict_students_data' is not defined

dict_students_data = {}

# Functions
# 1. dict()
d = dict()
# 2. len()

# 3. clear()

# 4. get()
dict_students_data = {
    "ram"  : 90,
    "shyam": 91,
    "sita" : 92,
    "geeta": 93,
}

print(dict_students_data.get("ram")) #90

# 5. pop()
dict_students_data.pop("ram")

print(dict_students_data) # {'shyam': 91, 'sita': 92, 'geeta': 93}
# dict_students_data.pop()
# print(dict_students_data) #TypeError: pop expected at least 1 argument, got 0

# 6. popitem()
print(dict_students_data.popitem()) # ('geeta', 93)
print(dict_students_data) #{'shyam': 91, 'sita': 92}


# 7. keys() : it return all key data
print(dict_students_data.keys()) #dict_keys(['shyam', 'sita'])
# 8. values()
print(dict_students_data.values()) #dict_values([91, 92])
# 9. items(): it returns list of tuples represnting key-value pair
for key,value in dict_students_data.items():
  print(key, " ", value)

# 10. copy(): it creates duplicate dictionary
d1 = dict_students_data.copy()
print(d1) #{'shyam': 91, 'sita': 92}
# 11. setdefault()
dict_students_data = {
    "ram"  : 90,
    "shyam": 91,
    "sita" : 92,
    "geeta": 93,
}
dict_students_data.setdefault("karan", 100)
print(dict_students_data) #{'ram': 90, 'shyam': 91, 'sita': 92, 'geeta': 93, 'karan': 100}
# 12. update()
