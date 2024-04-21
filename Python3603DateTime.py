# https://www.w3schools.com/python/python_datetime.asp
from datetime import *
import os
y = datetime.now()

# for i in range(100):
#     print(datetime.now()) # 2024-04-18 17:27:30.097509
#     os.system('cls' if os.name=='nt' else 'clear')

print(y.strftime("%d"))
print(y.strftime("%m"))
print(y.strftime("%Y"))

print(y.strftime("%H"))
print(y.strftime("%I"))
print(y.strftime("%S"))

print(y.strftime("%Y-%m-%d"))
