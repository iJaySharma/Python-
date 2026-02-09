#Arithmetic Operators

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

"""
Python has two division operators:

/ - Division (returns a float)
// - Floor division (returns an integer)
"""

#Python 3.8 introduced the := operator, known as the "walrus operator". It assigns values to variables as part of a larger expression:
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

#comparison operators return true or false based on comparison
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#Logical operator

x = 5
print(1 < x < 10)
print(1 < x and x < 10)

#Identity Operator
#is - Checks if both variables point to the same object in memory
#== - Checks if the values of both variables are equal
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

#Membership Operator
fruits = ["apple","banana","cherry"]
print("banana" in fruits)
print("pineapple" not in fruits)

#Bitwise Operator
print(6 & 3) #Sets each bit to 1 if both bits are 1
print(6 | 3) #Sets each bit to 1 if one of two bits is 1
print(6 ^ 3) #Sets each bit to 1 if only one of two bits is 1
print(~3) #Inverts all the bits
print(6 << 3) #Shift left by pushing zeros in from the right and let the leftmost bits fall off
print(6 >> 3) #Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
