# bytes data type

# x = [10, 20, 30, 40]
# b = bytes(x)
# #print(type(b)) #<class 'bytes'>
# print(b[0])


x = [10, 20, 30, 40]
b = bytes(x)
print(b[0])
b[0] = 10 #TypeError: 'bytes' object does not support item assignment


