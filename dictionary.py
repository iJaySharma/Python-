"""
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

Dictionaries are written with curly brackets, and have keys and values:

"""

thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(thisdict)

#print the brand value of the dictionary
print(thisdict["brand"])

#It is also possible to use the dict() constructor to make a dictionary.
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#There is also a method called get() that will give you the same result:
x = thisdict.get("name")
print(x)

#Get Keys 

#The keys() method will return a list of all the keys in the dictionary.

x = thisdict.keys()
print(x)
print(type(x))

thisdict["color"] = "white"

print(x)

#Get Values

x = thisdict.values()
print(x)
#same for value above example

x = thisdict.items()
print(x)
print(type(x))

if "name" in thisdict:
   print("Yes, 'name is one of the keys in the thisdict diction")


#Add a color item to the dictionary by using the update() method:
thisdict.update({"color":"red"})

