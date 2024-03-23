# checking starting and ending of string 
# it returns boolean value. 

#on success it return true
# on failure it return false

# 1. startswith
# 2. endswith

s = "python is a very good programming language"

print(s.startswith("python")) #True
print(s.startswith("Python")) #False

print(s.endswith("ming language")) #True
print(s.endswith("ming Language")) #False


# check the type of char in a string
# s1 = "python is a very good programming language"

# isalnum() -> check alphabets numerical values(A-Z , a-z , 0-9)
# isalpha() -> check alphabets (A-Z , a-z)
# isdigit() -> check numerical (0-9)
# islower() -> check lower case of char
# isupper() -> check upper case of char
# istitle() -> check title case of sting
# isspace() -> check if space exists in a string
print("-----")
s1 = "ABCD1234"

print("ABCD1234".isalnum()) #True
print("ABCD".isalpha())     #True
print("1234".isdigit())     #True
print("abcd".islower())     #True
print("ABCD".isupper())     #True
print("Abcd Def".istitle()) #True
print(" ".isspace())        #True


