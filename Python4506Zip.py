# zipping and unzipping of files
from zipfile import *
f = ZipFile("file.zip", "w", ZIP_DEFLATED)
f.write("1.txt")
f.write("2.txt")
f.write("3.txt")
f.close()

print("you files gets zipped")
