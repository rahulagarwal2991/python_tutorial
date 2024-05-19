# zipping and unzipping of files
# Python4507ZipExtract.py
# ZIP_DEFLATED -> zip operation
# ZIP_STORED -> UNZIP OPERATION
from zipfile import *
f = ZipFile("file.zip", "r",ZIP_STORED)
names = f.namelist()

for name in names:
    print(name)
    f1 = open(name, 'r')
    print(f1.read())