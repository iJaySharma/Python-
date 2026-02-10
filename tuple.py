#Tuple 
#A tuple is a collection which is ordered and unchangeable.Tuples are written with round brackets and can allow duplicates.

thistuple = ("apple","banana","cherry")
print(thistuple)

#A tuple can contain different data types:
tuple1 = ("abc", 34, True, 40, "male")

#Access Tuples by index and [] or range [:] same way as we do with list

#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
#Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


#To add item in it
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.

#Add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists

#Unpack Tuples
fruits  = ("apple","banana","cherry")
(green,yellow,red) = fruits 

print(green)
print(yellow)
print(red)

#Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# Loop Through a Tuple
#we can loop through tuple items by using a for loop
thistuple = ("apple","banana","cherry")
for x in thistuple: 
   print(x)

for i in range(len(thistuple)):
  print(thistuple[i])

i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# Join Two Tuples
#To join two or more tuples you can use the + operator:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#If you want to multiply the content of a tuple a given number of times, you can use the * operator:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

#count() Returns the number of times a specified value occurs in a tuple
#index() Searches the tuple for a specified value and returns the position of where it was found





