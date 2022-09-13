# Global Variables

from tkinter import Y


x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

def mynewfunc():
    global x
    x = "fantastic"
    
mynewfunc()

print("Python is " + x)