# identity Operators are used to compare the objects, not if they're equal, but if they're actually the same object, with the same memory location

# is :  Returns True if both variables are the same object  e.g (x is y)
# is not : Returns True if both variables are not the same object  e.g (x is not y)

# Here the operator returns true if both variables point to the same object

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)  # True
print(x is y)  # False
print(x == y)  # True


# The is not operator returns true if both variables do not point to the same object:

x = ["apple", "banana"]
y = ["apple", "banana"]
print(x is not y)


# Difference between is and ==
# is - Checks if both variables point to the same object in memory
# == - Checks if the values of both variables are equal

x = [1,2,3]
y = [1,2,3]

print(x == y)  # True
print(x is y)  # False