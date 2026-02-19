# Let's say you have a variable called "name" with your username in it, and you would then like to print(out a greeting to that user.)
# This prints out "Hello, John!"
print("1. \n")
name = "John"
print("Hello, %s!" % name)      # %s stands for string while %d stands for float

#To use two or more argument specifiers, use a tuple (parentheses):

# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age)) ()([[]])

# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)



# %s - String (or any object with a string representation, like numbers)
#
# %d - Integers
#
# %f - Floating point numbers
#
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

astring = "Hello world!"
astring2 = 'Hello world!'


astring = "Hello world!"
print("single quotes are ' '")

print('Don\'t')    # Escape character when using a single string...

# String Methods:
# len() returns the number of characters in a string...
print(len(astring))

#  index method : it returns the position of a particular character

astring = "Hello world!"
print(astring.index("o"))

# Count method : It counts returns how many times a character returns
astring = "Hello world!"
print(astring.count("l"))


# Slicing : Here we move a portion out of the original string
astring = "Hello world!"
print(astring[3:7])
print(astring[6:11])
print(astring[:])
print(astring[:5])
print(astring[5:])



astring = "Hello world!"
print(astring[1:7:2]) # el


astring = "Hello world!"
print(astring[::-1]) #reverse


astring = "Hello world!"
print(astring.upper())
print(astring.lower())



astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))



astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

lettersplit = list(astring)
print(lettersplit)


# Example: Using strip()

# Removes extra spaces from the beginning and end of a string
astring = "   Hello world!   "
print("Before strip:", astring)
print("After strip:", astring.strip())

# Removes specific characters from both ends of a string
text = ".!..!Hello World!!!..."
print(text.strip(".!"))


# split converts a string to list based on the value of the argument
letters = "Hel!lo w!orld H!ow a!re yo!u?"
print(letters.split("!"))


# Exercise 1: Email Validator
# Check if a string looks like an email (contains "@" and ends with ".com")
email = input("Enter your email: ")
if "@" not in email and email.endswith(".com"):
    print("Include '@'.")
elif(not email.endswith(".com") and "@" in email):
    print("Include '.com' at the end of email.")
elif(not email.endswith(".com") and "@" not in email):
    print("Include '@' and Include '.com' at the end of email!")
else:
    print("Valid Email!")



# Exercise 2: Password Strength Checker
# Check if a password has at least 8 characters and contains both upper and lowercase letters
password = input("Enter your password: ")
if len(password) >= 8 and password.lower() != password and password.upper() != password:
    print("Strong password!")
else:
    print("Weak password, try again.")


# Exercise 3: Word Counter
# Ask for a sentence and print each word with its character count
sentence = input("Enter a sentence: ")
words = sentence.split(" ")
for word in words:
    print("%s -> %d letters" % (word, len(word)))



# Exercise 4: Reverse and Check
# Reverse a word and check if it’s a palindrome (reads the same backward)
word = input("Enter a word: ")
reversed_word = word[::-1]
if word.lower() == reversed_word.lower():
    print("Palindrome word!")
else:
    print("Not a palindrome.")


# Exercise 5: Attendance List Formatter
# Convert a list of names into a formatted string for display
students = ["John", "Mary", "James", "Lisa"]
formatted = ""
for name in students:
    formatted += "%s, " % name
formatted = formatted.strip(", ")
print("Present students: %s"% formatted)