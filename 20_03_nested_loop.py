# WAP to print right angle triange using *, whose length = 5
# *
# **
# ***
# ****
# *****

# print("*")
# print("**")
# print("***")
# print("****")
# print("*****")
# *
# **
# ***
# ****
# *****

# print(1*"*")
# print(2*"*")
# print(3*"*")
# print(4*"*")
# print(5*"*")

# *
# **
# ***
# ****
# *****

# for i in range(1, 6):
#     print(i * "*")

# *
# **
# ***
# ****
# *****


for i in range(1,6):
    for j in range(1,i+1):
        print( j, end="")
    print()