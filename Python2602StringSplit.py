# spliting of string
# s1= s.split(seperator)
s ="This is a very long string"
print(s)
s1= s.split(" ")
for i in s1:
    print(i)
# This is a very long string
# This
# is
# a
# very
# long
# string


s ="This is a very long string"
print(s)
s1= s.split("a")
for i in s1:
    print(i)

# This is a very long string
# This is 
#  very long string

s ="This is a very long string"
print(s)
s1= s.split("i")
for i in s1:
    print(i)

# This is a very long string
# Th
# s 
# s a very long str
# ng