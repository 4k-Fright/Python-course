# Python Functions
# A function is a block of code which only runs when it is called.
#
# A function can return data as a result.

# A function helps avoiding code repetition.
#
# Creating a Function
# In Python, a function is defined using the def keyword, followed by a function name and parentheses:
#
# Example
def my_function():
    print("Hello from a function")


# This creates a function named my_function that prints "Hello from a function" when called.
#
# The code inside the function must be indented. Python uses indentation to define code blocks.
#
# Calling a Function
# To call a function, write its name followed by parentheses:
#
# Example
def my_function():
    print("Hello from a function")


my_function()


# You can call the same function multiple times:
#
# Example
def my_function():
    print("Hello from a function")


my_function()
my_function()
my_function()
# Function Names
# Function names follow the same rules as variable names in Python:
#
# A function name must start with a letter or underscore
# A function name can only contain letters, numbers, and underscores
# Function names are case-sensitive (myFunction and myfunction are different)
# Example
# Valid function names:

#  calculate_sum()
# _private_function()
# myFunction2()
# It's good practice to use descriptive names that explain what the function does.
#
# Why Use Functions?
# Imagine you need to convert temperatures from Fahrenheit to Celsius several times in your program. Without functions, you would have to write the same calculation code repeatedly:
#
# Example
# Without functions - repetitive code:

temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)


# With functions, you write the code once and reuse it:
#
# Example
# With functions - reusable code:

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))


# Return Values
# Functions can send data back to the code that called them using the return statement.
#
# When a function reaches a return statement, it stops executing and sends the result back:
#
# Example
# A function that returns a value:

def get_greeting():
    return "Hello from a function"


message = get_greeting()
print(message)


# You can use the returned value directly:
#
# Example
# Using the return value directly:

def get_greeting():
    return "Hello from a function"


print(get_greeting())


# If a function doesn't have a return statement, it returns None by default.
#
# The pass Statement
# Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:

# Example
def my_function():
    pass
# The pass statement is often used when developing, allowing you to define the structure first and implement details later.



# Exercise:
# Problem: Write a function convert_temp() that makes a temperature and a scale ("C" for Celsius, "F" for Fahrenheit).
# Convert it to the other scale and return the result

def convert_temp(value, scale):
    if scale == "C":
        return (value * 9 / 5) + 32
    elif scale == "F":
        return (value - 32) * 5 / 9
    else:
        return "Invvalid scale"

print(convert_temp(100, "C"))   # 212˚F



# ATM Withdrawal Simulator
# Problem: Create a function withdraw(balance, amount) that checks if the amount is less than or equal to the balance.
# If yes, subtract it and return the new balance; otherwise return "Insufficient funds".

def withdraw(balance, amount):
    if amount <= balance:
        balance -= amount
        return f"Withdrawal successful! New balance: ${balance}"
    else:
        return "Insufficient funds"
print(withdraw(5000, 2000))



# Password Strength checker
# Problem: Write a function that takes a password and checks: Length >= 8
# Contains at least one number
# Contains at least one uppercase letter
# Return "Strong", "Weak", or "Very weak"

def check_password(password):
    has_upper = any(ch.isupper() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)

    if len(password) >= 8 and has_upper and has_digit:
        return "Strong"
    elif len(password) >= 6:
        return "Weak"
    else:
        return "Very Weak"
print(check_password("Sammie1345"))



# Multiplication table generator
# Problem: Write a function multiplication_table(n) that prints the multiplication table of any number n up to 12.

def multiplication_table(n):
    for i in range(1, 13):
        print(f"{n} x {i} = {n * i}")

multiplication_table(10)