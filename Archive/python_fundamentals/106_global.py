# Script      : 106_global.py
# Description : 
# ------------------------------|| Global Variables ||-----------------------------
"""
Variables that are created outside of a function (as in all of the examples above) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.
"""
# //TODO Create a variable outside of a function, and use it inside the function
x = "Simple but powerful"

def myfistfunc():
    print("python is " + x)

"""
If you create a variable with the same name inside a function, this variable will be local,
 and can only be used inside the function.
The global variable with the same name will remain as it was, global and with the original value.
"""
# //TODO Create a variable inside a function, with the same name as the global variable

def mySecondfunc():
  x = "fantastic"
  print("Python is " + x)


myfistfunc()
mySecondfunc()
myfistfunc()
#print("Python is " + x)