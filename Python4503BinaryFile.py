# handling binary data
#Python4503BinaryFile.py
# ASCII Conversion Chart.gif

f1 = open("ASCII Conversion Chart.gif", "rb")
bytes = f1.read()


f2 = open("ascii_from_us1.gif", "wb")
f2.write(bytes)

f1.close()
f2.close()
print("new file copied")


