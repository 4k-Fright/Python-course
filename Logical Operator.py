# Logical Operators are used to combine conditional statements:


# and   Returns true if both statement are true   (x < 5 and x < 10)
# or    Returns true if one of the statements is true    (x < 5 or x < 4)
# not   Reverse the result, returns false if the result is true or not (x < 5 and x < 10)


# Here we test if a number is greater than 0 and less than 10:



x = 5

print(x > 0 and x < 10)


# Here we test if a number is less than 5 or greater than 10:

y = 5
print(y < 5 or y > 10)


# Here we reverse the result with not:

z = 5
print(not(z > 3 and z < 10))