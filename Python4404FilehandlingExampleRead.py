# Reading data from file

'''
read() -> to read total data from the file
read(n) -> read 'n' charcteres from a file 
readline() -> to read only one line
readlines() -> to read all lines in a list
'''

f = open("sales.txt", 'r')
# data = f.read()
# data = f.read(10)
# data = f.readline()
data = f.readlines()

print(data)