'''
File Handling
Types of files
1. Text File: we store char type of data
2. Binary File: here we store binary, video , audio, image etc

Dummy data
Sale amount , time
10000, 3 May 2024 1900 
5000, 3 May 2024 1910 
1000, 3 May 2024 1920 
'''

#opening a file:
'''
syntax:
f = open("filename", mode)
mode:
1. r -> r mode , read 
fileNotFoundError
2. w -> w mode , write mode
3. a -> a mode , append mode
4. r+ -> read and write.
5. w+ -> write and read. 
6. a+ -> append and read. 
7. x  -> create mode

b -> binary 
rb, wb, ab, r+b, w+b, a+b, xb

To close a file:
syntax
f.close()
'''

f = open("sales.txt", "w")

f.close()
