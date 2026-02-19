#  TUPLE
# A tuple is a collection of ordered, immutable elements in python.
# It's similar to a list, but you  can't change (modify) the values once defined
# Tuples are created by placing elements inside parenthesis ()

my_tuple =(10,20,30)
print(my_tuple)


# You can have a tuple without parenthesis using just commas:

my_tuple = 10,20,30,40,50
print(my_tuple)


# Tuple characteristics........
# Ordered: Items have a fixed position
# Immutable: You can't change items after creation
# Allow duplicates
# Can contain different data types


mixed_tuple = (1, "Hello", True, 3.5)
print(mixed_tuple)


# Tuple operations length: len(my_tuple)
# Count: my_tuple.count(value)
# Index: my_tuple.index(value)
# Slicing: my_tuple[1:3]

example = (5,10,15,20,10)
print(len(example))        # 5
print(example.count(10))    # 2
print(example.index(15))    # 2
print(example[::-1])      # (10 - 15)
print(example[0])         # 5



# Tuple unpacking
# You can assign tuple items to a variable directly:

a,b,c = (1,2,3)
print(a,b,c)



grade = (40,45,46,47,48,50)
grade1, grade2, grade3, grade4, grade5, grade6 = grade
print(grade4)


# Nested tuples
# Tuples can contain other tuples:

nested = ((1,2), (3,4))
print(nested[1][1])   # Output: 4





# When to use Tuples
# When data should not change (e.g. coordinates, constant settings).
# When you want faster performance
# As dictionary keys (tuples are parsable, lists are not).

# Tuple as dictionary keys
scores = {
    ("alice", "Math"): 85,
    ("bob", "Science"): 90,
    ("Alice", "Science"): 88
}

print(scores[("alice", "Math")])



# Exercise 1
# Tech (Software Licensing Tracker)
# Task: Create a dictionary using (user_email, software_name) as keys,and store the License expiration date as values.


# Add 3 entries.
# Update one expiry date


# Exercise 2
# Finance (Stock Portfolio)
# Task: Use (Investor_name, stock_symbol) as the key, and number of shares as value.

# Add 4 investor stock entries.
# Increase shares of one stock.
# Print total number of shares held by a specific investor.


# Exercise 3

# Health (Patient Check-in records)
# Task: Store check-in times using (patient_id, date) as the key, and time as the value.

# Exercise 4

# Add 5 students with different subjects and scores.
# Get a student's score in a particular subject.
# Calculate average score across all students


# Exercise 5
# 5. Industry (Machine Maintenance Records)
# Task: (Use machine_id, date) as key and status as value ("Serviced", "Pending", etc).

# Exercise:
# Add 4 maintenance entries.
# Change status of one machine.
# Count how many machines are pending service.


license_tracker = {
    ("frightog@gmail.com", "Netflix"): "2026/30/01",
    ("johndoe@gmail.com", "Myschool"): "2027/30/02"
}
print("Initial licence tracker: ")