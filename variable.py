# Variable is a container used to hold data
name = "Larry"
print(name)

# Python supports two types of numbers - integers(whole numbers) and floating point numbers(decimals). (It also supports complex numbers, which will be explained later as we go further).
# Integer
myint = 7
print(myint)

# Float
myfloat = 7.0
print(myfloat)

# converting Int to Float
floatnum = float(26) # typecasting
print(floatnum)


# Strings
# Strings are defined either with a single quote or a double quotes.

mystring = 'hello'
print(mystring)
stringtwo = "hello"
print(stringtwo)

#The difference between the two is that using double quotes makes it easy to include apostrophes (whereas these would terminate the string if using single quotes)
string3 = "Don't worry about apostrophes"
print(string3)

# Simple operators can be executed on numbers and strings:

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

#Assignments can be done on more than one variable "simultaneously" on the same line as this
a, b = 3, 4
print(a)
print(b)

firstName, lastName = "Larry", "Thomzy"
print(firstName)
print(lastName)
print(firstName,lastName)
print(firstName + lastName)




#Mixing operators between numbers and strings is not supported:

num1 = 1
num2 = 2
text = "hello"

# print(num1 + num2 + text)

#Boolean are true or false values
age = 25
is_hot = True
is_cold = False
is_adult = age >= 18

print(age)
print(is_hot)
print(is_cold)
print(is_adult)

#There are just a couple of rules to follow when naming your variables.
#Variable names can contain letters, numbers, and the underscore.
#Variable names cannot contain spaces
# Variable names cannot start with a number.
# Case matters—for instance, temp and Temp are different.
# Using descriptive names as your variables makes your program more understandable.




myName = "Larry"
print("My name is ", myName )
print("My age is", age)