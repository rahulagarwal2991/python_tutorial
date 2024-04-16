# Function aliasing

def sum(a, b):
    return a+b

print(sum(10, 15))

adddition = sum

print(adddition(10, 12))

print(id(sum))
print(id(adddition))