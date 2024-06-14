#Create a variable outside of a function, and use it inside the function

x = "jerin"

def myfunc():
  print("My name is " + x)

myfunc()

#To create a global variable inside a function, you can use the global keyword.

def myfunc():
  global x
  x = "jerin"

myfunc()

print("my name is " + x)
