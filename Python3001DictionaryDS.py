# Dictionary: If we want to present a group of objects as key-value pair 
# then we need to use dictionary DS.

Dict = {"key": "value"}

dict_students_data = {
  "user_1": 90,
  "user_2": 91,
  "user_3": 92,
  "user_4": 93,
}

dict_students_data = {
  "user_2": {"english" : 90,"hindi" : 80,"maths" : 90,"science" : 90,"sst" : 90,},
  "user_3": {"english" : 90,"hindi" : 80,"maths" : 90,"science" : 90,"sst" : 90,},
  "user_1": {"english" : 90,"hindi" : 80,"maths" : 90,"science" : 90,"sst" : 90,},

  
}

# Features
# Duplicate keys not allowed
# Hatrogenious object are allowed
# order is not preserved
# dicionary is mutable
# indexing and slicing is not applicable

# how to create a dictionary

# d = {}
d = dict()
print(type(d))
# process of adding the data
d["english"] = 100 # {'english':100}
d["hindi"] = 100 #{'english': 100, 'hindi': 100}

print(d) #{'english': 100, 'hindi': 100}
 
d1 =  {'english': 100, 'hindi': 100}
print(d1)

# access a value using key from dictionary
print(d1['hindi']) # 100