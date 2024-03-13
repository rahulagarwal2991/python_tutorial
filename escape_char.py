# escape characters
#ex 1
from re import T


s = "geeks with geeks"
print(s)

#ex 2
s = "geeks \nwith \ngeeks"
print(s)

#ex 3
s = "geeks\twith\tgeeks"
print(s) #geeks   with    geeks

#ex 4
s = "geeks \"with\" geeks"
print(s) #geeks "with" geeks


#ex 5
s = "geeks \\\"with\\\" geeks"
print(s) #geeks \"with\" geeks


# \n
# \t
# \r
# \b
# \f
# \v
# \'
# \"
# \\

