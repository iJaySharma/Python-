#Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])

#Since strings are arrays, we can loop through the characters in a string, with a for loop.Loop through the letters in the word "banana":
for x in "banana":
   print(x)

#The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))

#To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt)

#Use it in an if statement:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
txt = "The best things in life are free!"
print("expensive" not in txt)

#Use it in an if statement:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#Get the characters from position 2 to position 5 (not included):
b = "Hello, World"
print(b[2:5])

#Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])

#Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])

a = " Hello, World! "
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("H","J"))
print(a.split(","))

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)


#age = 36
#This will produce an error:
#txt = "My name is John, I am " + age
#print(txt)

#F string
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Perform a math operation in the placeholder, and return the result:

txt = f"The price is {20 * 59} dollars"
print(txt)


#The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."

a = "Hello"
b = "Jay"
print(a+b)


















