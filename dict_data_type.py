#Dict data type
d ={ 5 : "Geeks", 2: "with", 3: "geeks"}
print(type(d)) #<class 'dict'>
print(d[5]) #Geeks

d ={"5": "Geeks", "2": "with", "3": "geeks"}
print(type(d)) #<class 'dict'>
print(d["5"]) #Geeks

d ={"a": "Geeks", "b": "with", "c": "geeks"}
print(type(d)) #<class 'dict'>
print(d["b"]) #with
d["b"] = "data"
d["d"] = "data"
print(d) # {'a': 'Geeks', 'b': 'data', 'c': 'geeks', 'd': 'data'}

del d["d"]
print(d) #{'a': 'Geeks', 'b': 'data', 'c': 'geeks'}
del d["b"]
print(d) #{'a': 'Geeks', 'c': 'geeks'}