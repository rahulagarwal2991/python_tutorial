# Relational Operator > >= < <=
a = 10
b = 20
print(a > b)  # 10 greater than 20  :  no or False
print(a >= b) # 10 greater than or equal to 20  : False
print(a < b)  # 10 is small than 20 : yes or True
print(a <= b) # 10 is smaller than or equal to 20 : True


a = 10
b = 10
print(a > b)  # False | False
print(a >= b) # True  | True
print(a < b)  # False | False
print(a <= b) # True  | True


####### String type comparision
str1 = "Geeks"
str2 = "Geeks"
print(str1 > str2)  # False
print(str1 >= str2) # True
print(str1 < str2)  # False
print(str1 <= str2) # True

####### String type comparision
str1 = "Geeks" 
str2 = "Geekt"
print(str1 > str2)  # False
print(str1 >= str2) # False
print(str1 < str2)  # True
print(str1 <= str2) # True


####### String type comparision
str1 = "Geeks"
str2 = "Geeks1"
print(str1 > str2)  # False
print(str1 >= str2) # False
print(str1 < str2)  # True
print(str1 <= str2) # True

print(True > False)  # True
print(True >= False) # True
print(10 >= False)   # 10 >=0 : True
# print(10 >= "GWG")   #TypeError: '>=' not supported between instances of 'int' and 'str'

######Chaining Relational Operator
c = 10 < 20 < 30 < 40
print(c) #True

c = False < 20 < 30 < 40
print(c) #True

c = 10 < 20 < 30 < 40  > 50
print(c) # False

c = 10 > 20 < 30 < 40  < 50
print(c) # False
print("------")

# Equality Operator == !=
print(10 == 10) # True
print(10 == 11) # False
print(True == False) # False
print(True == True) # True
print("GWG" == "GWG") # True
print(10 == "GWG")# False

print(10 != 10) # Fale
print(10 != 11) # True
print(True != False) # True
print(True != True) # False
print("GWG" != "GWG") # False
print(10 != "GWG")# True

print("10" == 10) # False
print("10" != 10) # True
print("------")
# Chaning 
print(10 == 20 == 10 == 10) # False

print(10 == 10 == 10 == 10) # True


Relational operator

1. Basic Comparisons:
Write a program that compares two numbers and prints whether they are equal, greater than, or less than each other.
Write a program that checks if a given number is positive, negative, or zero.
Write a program that compares two strings and prints whether they are equal, lexicographically smaller, or lexicographically larger.

2. Conditional Statements:
Write a program that determines if a given number is within a specific range (e.g., between 10 and 20).
Write a program that checks if a character is uppercase, lowercase, or a number.
Write a program that simulates a simple guessing game where the user has to guess a hidden number within 3 attempts.

3. Logical Operators:
Write a program that checks if a given number is even and greater than 10 using both and and or operators.
Write a program that simulates a login system where the user must enter a correct username and password to access the system.
Write a program that checks if a given year is a leap year. A leap year is defined as:
Any year divisible by 4 is a leap year. However,
Years divisible by 100 but not by 400 are not leap years.

4. String Manipulation (Bonus):
Write a program that checks if a given string starts with a specific character.
Write a program that checks if a given string contains a specific substring.
Write a program that checks if a given string is a palindrome, meaning it reads the same backward as forward (e.g., "level", "madam").

5. Challenge:
Write a program that analyzes three numbers and determines the largest and smallest among them using relational and logical operators.
Write a program that simulates a simple quiz with multiple choice questions. The program should use conditional statements based on user input to check answers and provide feedback.
Write a program that validates user input in a specific format, such as an email address or a phone number, using regular expressions and relational operators.