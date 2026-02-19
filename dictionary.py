# Dictionary
# Dictionaries are used to store data values in key:value pairs.
#
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates

# Dictionaries are written with curly brackets, and have key and values:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# Dictionary items
# Dictionary items are ordered, changeable and do not allow duplicates

# Dictionary items are presented in key:value pairs, and can be referred to by using the key name

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])

# Ordered or Unordered?

# As part of python version 3.7, dictionaries are ordered, in python 3.6 and earlier, dictionaries are unordered

# When we say dictionaries are ordered, it means that the items have a defined order, and that order will not change

# Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.

# Changeable...
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created

# Duplicates are not allowed
# Dictionaries cannot have two items with the same key

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)


# Dictionary length
# To determine how many items a dictionary have use the len() function:
print(len(thisdict))


# Dictionary Items - Data types
# The values in dictionary items can be of any data type:

thisdict ={
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(thisdict)

# type()
# Fron Python's perspective, dictionaries are defined as objects with the data type 'dict' :







# Using the dict() constructor method to make a dictionary:

thisdict = dict (name = "John", age = 36, country = "Norway")
print(thisdict)




# Accessing items
# You can access the items of a dictionary by referring to its key name, inside square brackets:



car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car["model"]
print(x)


# There's also a method called get() that will give you the same result

y = car.get("brand")
print(y)


# Get keys
# The keys() method will return a list of all the keys in the dictionary

x = car.keys()
print(x)

# Add a new item to the original dictionary, and see that the key lists gets updated as well:

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()
print(x)  # before the change

car["color"] = "white"

print(x)   # after the change


# Get values
# The values() method will return a list of all the values in the dictionary

x = thisdict.values()
print(x)
# Make a change in the original dictionary, and see that the value lists gets updated as well:


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()
print(x)   # before the change

car["year"] = 2020
print(x)   # after the change



# # Add a new item to the original dictionary, and see that the key lists gets updated as well:


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()
print(x)   # before the change

car["color"] = "red"
print(x)  # after the change



# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.

x = car.keys()
print(x)

# Check if "model" is present in the dictionary:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in thisdict dictionary")




# Change values
#  You can change the value of a specific item by referring to its key name:

car2 = {
    "brand": "Lambhorgini",
    "model": "Urus",
    "year": 2024
}
car2["ÿear"] =2026
print(car2)




# Update Dictionary
# The update method will update the dictionary with the item from the given argument.
#
# Update the "year" of the car by using the update() method:

thisDict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
thisDict.update({"year": 2020})
print(thisDict)



# Adding items
# Adding an item is the dictionary is done by using a new index key ad assigning a value to it:

thisDict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
thisDict["color"] = "red"
print(thisDict)

# Update Dictionary
# The Update() method will update the dictionary with the items from a given argument. if the item does not exist, the item will be added.
#
# The argument must be a dictionary, or an iterable object with key:value pairs

thisDict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
thisDict.update({"color" : "red"})

# Removing items
# There are several methods to remove items from a dictionary:

# The pop() method removes the item with the specified key name:
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1964
}
thisDict.pop("model")
print(thisDict)

# The popitem() method removes the inserted item (in versions before 3.7, a random instead):
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1964
}
thisDict.popitem()
print(thisDict)

# The del keyword removes the item with the specified key name:

thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1964
}
del thisDict["model"]
print(thisDict)

# The del keyword can also delete the dictionary completely:

thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1964
}

# del thisDict
print(thisDict) # this will cause an error because "thisDict" no longer exists

# The clear() method empties the dictionary
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1964
}
# thisDict.clear()
print(thisDict)

#
# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop/
#
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well

# This print all key names in the dictionary, one by one:

for x in thisdict:
    print(x)

# This print all key names in the dictionary, one by one:
for x in thisdict:
    print(thisdict[x])

# You can use the value method to return values of a dictionary:
for x in thisDict.values():
    print(x)

# You can use the key() method to return values of a dictionary:
for x in thisDict.items():
    print(x)

# Loop through both keys and values, by using the items() method:
for x, y in thisDict.items():
    print(x, y)


# Copy a dictionary
# You cannot copy a dictionary simple by typing dict2 = dict1, because: dict2 will only be a reference in dict1, and changes made in dict1 will automatically also be made in dict2
#
# There are ways to make a copy, one way is to use the built-in Dictionary method copy()

# Here we make a copy of a dictionary with the copy() method:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)



# Another way to make a copt is to use the built-in function dict().
# Here we make a copy of a dictionary with the dict() function:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)


# Nested Dictionaries
# A dictionary can contain dictionaries, this is called Nested Dictionaries.

# Here we create a dictionary that contains three dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
    },
    "child2" : {
      "name" : "Tobias",
      "year" : 2007
    },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
    }
}


# Or if you want to add three dictionaries into a new dictionary:
# Here we created three dictionaries, then create one dictionary that will containbthe other three dictionaries
child1 = {
    "name" : "Emil",
    "year" : 2004
}
child2 = {
    "name" : "Tobias",
    "year" : 2007
}
child3 = {
    "name": "Linus",
    "year" : 2011
}
myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}

# Access items in nested dictionaries
# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
# Here we print the name of child 2:
print(myfamily["child2"]["name"])


# Loop through nested dictionaries
# You can loop through a dictionary using the items() method like this
# Loop through the keys and values of all nested dictionaries:
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])



# Dictionary methods
# Python has a set of built-in methods you can use in dictionaries

# clear() : Removes all the elements from the dictionary
# copy() : Returns a copy of the dictionary
# fromkeys() : Returns a dictionary with the specified keys and value
# get() : Returns the value of the specified key
# items(): Returns a list containing a tuple for each key value pair
# keys(): Returns a list containing the dictionary keys
# pop(): Removed the element with the specified key
# popitem(): Removes the last inserted key-value pair
# setdefault(): Returns the value of the specified key,if the key doesn't exist, insert the key with the specified value
# update() : Updates the dictionary with the specified key-value pairs
# values() : Returns a list of all the values in the dictionary.