# Python4402FilehandlingExample.py
'''
name
mode
closed
readable()
writable()
'''
f = open("sales.txt", 'w')
print("file name ", f.name)
print("File mode ", f.mode)
print("File closed ", f.closed)
print("File readable() ", f.readable())
print("File writable() ", f.writable())



f.close()