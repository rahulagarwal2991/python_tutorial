'''
# Python4303Ex.py
# predefined exceptions
# 10/0 -> ZeroDivisionError

# userdefined exceptions
'''

class TooYoungToVoteException(Exception):
     def __init__(self, arg):
         self.msg = arg


age = 16 

if(age < 18):
    raise TooYoungToVoteException("Your age is smaller than 18 years")
else :
    print("You are eligible")
