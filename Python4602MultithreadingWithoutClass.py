# Python4602MultithreadingWithoutClass.py

from threading import *

def display():
    for i in range(1, 11):
        print("child thread")

t = Thread(target=display) # create a thread
t.start() # start a thread

for i in range(1, 11):
    print("Main thread")
'''
child thread
Main thread
Main thread
child thread
child thread
Main thread
Main thread
Main thread
Main thread
Main thread
Main thread
Main thread
Main thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread

'''