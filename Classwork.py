# Write a program that generates a list L of 10 random numbers between
# Replace each element in a list L with its square
# 2. Count how many items in a list L are greater than 50.
# Exercise 3: Word Counter
# Ask for a sentence and print each word with its character count


import random

# Generate list of 10 random numbers between 1 and 100
L = [random.randint(1, 100) for i in range(10)]

print("Random Numbers list:", L)

# Replace each element with its square
L = [x**2 for x in L]

print("Squared list:", L)

# Count how many items are greater than 50
count = 0
for x in L:
    if x > 50:
        count += 1

print("Number of items greater than 50:", count)



# Ask for a sentence
sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

# Print each word with its character count
for word in words:
    print(word, "=", len(word), "characters")




# ===============================================================================================


# Shopping Discount System
#
# Problem:
# Write a function calculate_discount(price) that applies discounts:
#
# If price > 5000 → 20% off
#
# If price > 2000 → 10% off
#
# Otherwise → no discount
# Even and Odd Counter
#
# Problem:
# Write a function that takes a list of numbers and returns how many are even and how many are odd.


def calculate_discount(price):
    if price > 5000:
        return price * 0.8
    elif price > 2000:
        return price * 0.9
    else:
        return price
print(calculate_discount(6000))
print(calculate_discount(3000))
print(calculate_discount(1500))


def count_even_odd(numbers):
    even = 0
    odd = 0

    for num in numbers:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd
nums = [1, 2, 3, 4, 5, 6]
print(count_even_odd(nums))