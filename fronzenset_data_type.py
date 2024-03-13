# fronzenset data type
s = {10, 20, 30, 40, 50}
print(type(s)) #<class 'set'>
frozens = frozenset(s)
print(frozens)
print(type(frozens)) #<class 'frozenset'>
# share response of add and remove function
