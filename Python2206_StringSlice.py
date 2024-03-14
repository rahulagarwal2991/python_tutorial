#slice operator
# syntax : s [bEngineIndex:endindex:step]
# bEngineIndex : from where we have to start
# endindex : ending point at (endindex -1)
# step : jump

s = "This is a very good day"
str_output = s[1:4]
print(str_output) # his
str_output = s[0:4]
print(str_output) # This

str_output = s[10:14]
print(str_output) # very

str_output = s[10:19]
print(str_output) # very good

str_output = s[10:17:1]
print(str_output) # very go

str_output = s[10:17:2]
print(str_output) # vr o

A
B
C
D
E