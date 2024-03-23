# Removing spaces from string

# rstrip -> remove space from RHS
# lstrip -> remove spaces from LHS
#  strip -> remove spaces from both side

string = "   Btech institute     "
print(len(string)) # 23

string_1 = string.rstrip()
print(len(string_1)) # 18

string_2 = string.lstrip()
print(len(string_2)) # 20

string_3 = string.strip()
print(len(string_3)) # 15


