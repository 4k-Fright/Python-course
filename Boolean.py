# Boolean represents one or two values: True or False.

# Boolean values
# In programming you often need to know if an expression is true or false.

#  You can evaluate any expression in python, and get one of two answers, True or False.

# When you compare two values, the expression is evaluated and Python returns the Boolean answer:


print(10 > 9)  # True
print(10 == 9)  # False
print(10 < 9)  # False


# When you run a condition in an if statement, Python returns True or False:
a = 200
b = 33


# Print a message based whether the condition is true or false:
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")


# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return.

# Evaluate a string or number:

print(bool("Hello"))
print(bool(15))


x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Most values are True
# Almost any value is evaluated to True if it has some sort of content.

# Any string is true except empty strings

# Any list, tuple, set and dictionary are true except empty ones


# THe following will return true:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


# Some values are false
# In fact, there are not many values that evaluate to false, except empty values such as, # (), [], {}, "", the number 0, and the value None.
# And ofcourse the value False evaluates to False.


# The following will return false:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})