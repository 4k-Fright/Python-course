# Python conditions and If statements
# Python supports the usual logical conditions from other mathematics:
#
# Equals:   a == b
# Not Equals:   a != b
# Less than:   a < b
# Greater than:   a > b
# Greater than or equal to:   a >= b


# These conditions can be used in several ways, most commonly "if statements" and loops.
#


# An "if statement" is written by using the if keyword.


a = 33
b = 200
if b > a:
    print("b is greater than a")

# Checking if a number is positive:

number = 15
if number > 0:
    print("The number is positive")


# Indentation
# Python relies on indentation (white space at the beginning of a line) to define scope in the code
# Other programming languages often use curly-brackets for this purpose


# If statement, without indentation (will raise an error):
a = 33
b = 200
if b > a:
    print("b is greater than a")   # you'll get an error

# Note: You can use spaces or tabs for indentation, but you must use the same amount of indentation for all statements within the same code block.



# You can have multiple statements inside an if block. All statements must be indented at the same level
# Multiple statements in an if block:

age = 20
if age >= 18:
    print("You're an adult")
    print("You can vote")
    print("You have full legal rights")



# Boolean variables can be used directly in if statements without comparison operators.
# Using boolean variables:
is_logged_in = True
if is_logged_in:
    print("You are logged in")

# Python can evaluate many types of values as True or False in an if statement.

# Zero (0), Empty strings (""), None and empty collections are treated as False. Everything else is treated as True.

# This includes positive numbers (5), negative numbers (-3), and non-empty string (even "False" is btreated as True because it's a non-empty string).


# The Elif keyword
# The Elif keyword is Python's way of saying "if the conditions were not true", then try this condition

# The Elif keyword allows you to check multiple expressions for True and execute aa block of code as soon as one of the conditions evaluates to True.

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# Multiple Elif statements
# You can have as many elif statements as you need. Python will check each condition in order and execute the first one that is true

score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B)")
elif score >= 70:
    print("Grade: C)")
elif score >= 60:
    print("Grade: D)")

# Important: Only the first true condition will be executed. Even if multiple conditions are true, Python stops after executing the first matchung block.

age = 25

if age < 13:
    print("You're a child")
elif age < 20:
    print("You're a teenager")
elif age < 65:
    print("You're an adult")
elif age >= 65:
    print("You're a senior")

# When to use Elif.
# Use elif when you have multiple mutually exclusive conditions to check.
# This is more efficient than use multiple seoerate if statements because Python stops checking once it finds a true condition.
# Day of the week checker:

day = 3
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")



# The else keyword
# The else keyword catches anything which isn't taught by the preceeding conditions
#
# The else statement is executed when the if condition (and any elif conditions) evaluate to False.

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# Else without Elif
# You can also have an else without the elif:

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# This creates a simple two-way choice: If the condition ius true, execute one block: otherwise, execute the else block.


# How Else Works
# The else statement provides a default action when none of the previous conditions are true
# Think of it as a "catch-all" for any scenario not covered by your if and elif statements.


# Note: The else statement must come. You cannot have an elif after an else.
# Checking even or odd numbers:

number = 7
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


# You can combine if,  elif, and else to create a comprehensive decision-making structure.

# Temperature classifier:

temperature = 22

if temperature > 30:
    print("It's hot outside!")
elif temperature > 20:
    print("It's warm inside!")
elif temperature > 10:
    print("It's cool outside!")
else:
    print("It's cold outside!")


# Short Hand If
# If you have only one statement to execute, you can put uit on the same line as the if statement

a = 5
b = 2
if a > b: print("a is greater than b")   # This is called One-line if statement

# Note: You still need the colon : after the condition.

# Short hand IF ... Else
# If you have one statement each for if and else, you can put them on the same line using a conditional expression:
a = 2
b = 330
print("A") if a > b else print("B")     # This is what we call One-line if/else statement
# It's also called a conditional expression (sometimes known as a "ternary operator").


# Assign avalue with IF ... Else
# You can also use one-line if/else to choose a value and asign it to a variable:

a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)
# The syntax follows  this pattern:
# Variable = value_if_true if conditoon else value_if_false

# Multiple conditions on One line
# You can chain conditional expressions, but keep it short so it stays readable:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


# Pratical examples
# Tenary operators are particularly useful for simple assignments and return statements.

# Finding the maximum of two numbers:
x = 15
y = 20
max_value = x if x > y else y
print("Maximum value is ", max_value)


# Setting to a default value:
username = ""
display_name = username if username else "Guest"
print("Welcome ", display_name)


# When to use Shorthand If
# Shorthand if statements and ternary operators should be used when:
#
# The condition and actions are simple
# It improves code readability
# You want to make a quick assignment based on a condition


# Important: While shorthand if statements can make code more concise, avoid overusing them for complex conditions
# For readability, use regular if-else statements when dealing with multiple lines of code or complex logic.


# Python Logical Operators
# Logical operators are used to combine conditional statements. Pythonhas three logical operators
#
# and - rReturns True if both statement are true
# or - Returns True if one of the statements is true
# not - Reverses the result, returns False if the result is true


# The and operator
# The and keyword is a logical operator, and is used to combine conditional statements. Both conditions must be true for the entire expression to be tryue

# Test if a is greater than b, AND if c is greater than a:

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are true")


# The or Operator
# It's a logical operator, and is used to combine conditional statements. At least one condition must be true for the entire expression to be true

# Test if a is greater than b, OR if a is greater than c:
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is true")


# The not Operator
# It's a logical operator, and is used to reverse the result of the conditional statement.

# Test if a is NOT greater than b:
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")


# Combining Multiple Operators
# You can combine multiple logical operators in a single expression. Python not first, then and, then or.

# Combining and, or and not:
age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
    print("Discount applies!")


# Using Parentheses for Clarity
# When combining multiplr logical operators, use parentheses to mske your intentions clear and control the order of evaluation


# Using parentheses for complex conditions:
temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
    print("Great day for outdoor activities!")


# User authentication check:
username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
    print("Login successful!")
else:
    print("Login failed")



# Range checking with logical operators:
score = 85

if score >= 0 and score <= 100:
    print("Valid score")
else:
    print("Invalid score")



                         # Nested If Statements
# You can have if statements inside if statements. This is called ☝️☝️

x = 41

if x > 10:
    print("Above 10,")
if x > 20:
    print("and also above 20,")
else:
    print("but not above 20,")

# In this example, the inner if statement only runs if the outer condition (x > 10) is true.


# How Nested If works
# Each level of nesting creates a deeper level of decision-making. The code eveluates from the outermost condition inward.

# Checking multiple conditions with nesting:

age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You're too young to drive")


# Multiple levels of Nesting
# You can nest as many levels deep as needed, but keep in mind that too many levels can make code harder to read

# Three levels of Nesting

score = 85
attendance = 90
submitted = True

if score >= 60:
    if attendance >= 80:
        if submitted:
            print("Pass with good standing")
        else:
            print("Pass but missing assignment")
    else:
        print("Pass but low attendance")
else:
    print("Fail")


# Nested if vs Logical Operators
# Sometimes nested if statements statements can be simplified using logical operators like and. The choice depends on your logic.

# This nested if:
temperature = 25
is_sunny = True

if temperature > 20:
    if is_sunny:
        print("Perfect beach weather!")


# Could also be written with and:
temperature = 25
is_sunny = True

if temperature > 20 and is_sunny:
    print("Perfect beach weather!")


# Both approaches produce the same result. Use nested if statements when the inner logic is complex or depends on the outer condition. Use and when both conditions are simple and equally important

# Login validation with nested checks:

username = "Emil"
password = "python123"
is_active = True

if username:
    if password:
        if is_active:
            print("Login successful!")
        else:
            print("Account not active")
    else:
        print("Password required")
else:
    print("Username required")



# Grade calculation with nested logic:

score = 92
extra_credit = 5

if score >= 90:
    if extra_credit > 0:
        print("A+ grade")
    else:
        print("A grade")
elif score >= 80:
    print("B grade")
else:
    print("C grade or below")


# The pass Statement
# if statments cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

a = 33
b = 200

if b > a:
    pass


# The pass statement is a null operation - nothing happens when it executes. It serves as a placeholder.

# Why use pass?
# The pass statement is useful in several situations:
#
# When you're creating code structure but haven't implemented the logic yet
# When a statement is required syntactically but no action is needed
# As a placeholder for future code during development
# In empty functions or classes that you plan to implement later



# pass in Development
# During development, you might want to sketch out your program structure before implementing the details. The pass statement allows you to do this without syntax errors.

age = 16

if age < 18:
    pass # TODO: Add underage logic later
else:
    print("Access granted")


# pass vc Comments
# A comment is ignored by Python, but pass is actual statement that gets executed (Though it does nothing).
# You need pass where Python expects a statement, not just a comment.


# This will cause an error (empty code block)
score = 85

# if score > 90:
    # This is excellent
# This will raise an indentation error

# This works correctly with pass:
score = 85

if score > 90:
    pass # This is excelent
print("Score processed")

# pass with Multiple  onditions
# You can use pass in any branch of an if-elif statement.
# Using pass in different branches:
value = 50

if value < 0:
    print("Negative value")
elif value == 0:
    pass # Zero case - no action needed
else:
    print("Positive value")


# pass in other contexts
# While we focus on pass with if statements here, it's also commonly used with loops, functions, and classes.

# Using pass with functions:

def calculate_discount(price):
    pass # TODO: Implement discount logic

# Function exists but doesn't do anything yet


# Exercises:
# Create a variable age with the value 20
# Write an if statement that prints "Child" if age is less than 13
# Add an elif that prints "Teenager" if age is less than 18
# Add an else that prints "Adult"
# Create a variable score with the value 85
# Use a shorthand if to print ''Pass" if score is greater than or equal to 50

age = 20

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")


score = 85

if score >= 50: print("Pass")