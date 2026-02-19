#Comparison Operators are used to compare two values:


# == Means Equals to        e.g (x == y)
# != Not equal    e.g (x = y)
# > Greater than   e.g (x > y)
# < Less than     e.g (x < y)
# >= Greater than or equal to    e.g (x >= y)
#<= Less than or equal to     e.g (x <= y)


# Comparison operators return true or false based on the comparison

x = 5
y = 3

print(x == y)   # false
print(x != y)   # true
print(x > y)    # true
print(x < y)    # false
print(x >= y)   # true
print(x <= y)   # false


# Chaining Comparison operators

# Python allows you to chain Comparison Operators

x = 5
print(1 < x < 10)   # true

print(1 < x and x < 10)   # true