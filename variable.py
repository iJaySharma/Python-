#Python has no command for declaring a variable.

#A variable is created the moment you first assign a value to it.
x = 5
y = "John"
print(x)
print(y)

#Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y))

"""
Rules for Python variables:

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""

"""
This are invalid 
2myvar = "John"
my-var = "John"
my var = "John"
"""

#Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
#Unpack a list:

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#You can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
"""
x = 5
y = "John"
print(x + y)
"""
#Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.


#Create a variable outside of a function, and use it inside the function
x="awesome"

def myfunc():
   print("Python is "+x)

myfunc()

#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.To create a global variable inside a function, you can use the global keyword.

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


