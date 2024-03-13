# set data type
#index concept is not applicable
s = {100, 0, 10, 200, 10,  "GWG"}
print(s) # {0, 100, 200, 10, 'GWG'}

print(type(s)) #<class 'set'>

print(s[0]) #TypeError: 'set' object is not subscriptable

# add / remove
s.add("Anshul") 
print(s) # {0, 'Anshul', 100, 200, 10, 'GWG'}

s.remove(10)
print(s) #{0, 'Anshul', 100, 200, 'GWG'}

s = {100, 0, 10, 200, 10,  "GWG"}
s.add(100)
print(s) #{0, 100, 200, 10, 'GWG'}

t = {100, 100, 0, 10, 200, 10,  "GWG"}
print(t) #{0, 100, 200, 10, 'GWG'}

