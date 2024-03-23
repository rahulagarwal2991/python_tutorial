# String replacement 
s = "Python is very difficult language"
print(s)
# s.replace(oldsubstring, newsubstring)
s1 = s.replace("difficult", "easy")
print(s1)
#Pyhton is very difficult language
#Pyhton is very easy language


s1 = s.replace("Python is very difficult language", "easy")
print(s1)
#Python is very difficult language
#easy



s1 = s.replace("a", "-easy-")
print(s1)
print(id(s)) #4382098128
print(id(s1)) #4382098512
# easy
# Python is very difficult l-easy-ngu-easy-ge

s1 = s.replace("Pythons is very difficult language", "-easy-")
print(s1)
#Python is very difficult language


