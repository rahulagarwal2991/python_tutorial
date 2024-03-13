# Arithmetic operators
# + => addition
# - => subtration
# * multiplication
# / division
# % modulus
# //  floor division
# ** power or exponential

a = 10
b = 2
# + => addition
c = a + b
print(c) #12

a = 10
b = 2
# - => subtraction
c = a - b
print(c) #8

a = 10
b = 2
# * => multiplication
c = a * b
print(c) #20

a = 10
b = 2
# / => division
c = a / b
print(c) #5


a = 10
b = 0
# / => division
c = a / b
print(c) # ZeroDivisionError: division by zero



a = 11
b = 2
# % => modulus
c = a % b
print(c) #1


a = 11
b = 0
# % => modulus
c = a % b
print(c) # ZeroDivisionError: division by zero


a = 11
b = 3
# ** => power
c = a ** b # 11 * 11 *11
print(c) #1331


a = 11
b = 3
# // => floor division
c = a // b 
print(c) #3

#######
print(10/5)    # 2.0
print(10//5)   # 2
print(10.0/5)  # 2.0
print(10.0//5) # 2.0
print(10.0//5.0) # 2.0


######
# + , * 
a = "ram"
b = 2
# print(a+b) # TypeError: can only concatenate str (not "int") to str

a = "ram"
b = "2"
print(a+b) # ram2

a = 10
b = 2
print(a+b) # 12

a = "10"
b = "2"
print(a+b) # 102

# * 
value = " bharat "
times = 2
output = value * times
print(output) # bharat  bharat 

output = times * value
print(output) # bharat  bharat 


value = " bharat \n"
times = 2
output = value * times
print(output)
# bharat 
#  bharat 


value = " bharat \n"
times = " bharat \n"
output = value * times
# print(output) # TypeError: can't multiply sequence by non-int of type 'str'

value = " bharat \n"
times = 2.5
output = value * times
# print(output) # TypeError: can't multiply sequence by non-int of type 'str'

# + string concatination op
# * string multiplication op



1. Basic Calculations:
Write a program that prompts the user for two numbers and then prints their sum, difference, product, and quotient (division).
Write a program that calculates the area of a rectangle and the volume of a cube, given their side lengths.
Write a program that converts Celsius temperature to Fahrenheit and vice versa, using the formulas:
Fahrenheit = (Celsius * 9/5) + 32
Celsius = (Fahrenheit - 32) * 5/9

2. Modulo Operator:
Write a program that determines if a number is even or odd using the modulo operator (%).
Write a program that finds the remainder after dividing two numbers.
Write a program that simulates a simple dice roll (1-6) using the modulo operator.

3. Exponents and Floor Division:
Write a program that calculates the square and cube of a number using the exponent operator (**).
Write a program that calculates the integer quotient of two numbers using the floor division operator (//).
Write a program that finds the number of digits in a given integer.

4. String Manipulation (Bonus):
Write a program that combines two strings using the addition operator (+).
Write a program that repeats a string a specific number of times using multiplication operator (*).
Write a program that extracts a specific substring from a given string using indexing.

5. Challenge:
Write a program that calculates the area of a triangle given its base and height using the formula: area = (base * height) / 2.
Write a program that calculates the body mass index (BMI) of a person given their weight and height using the formula: BMI = weight (kg) / height (m)^2.
Write a program that checks if a given number is a prime number. A prime number is a natural number greater than 1 that has exactly two positive divisors: 1 and itself.