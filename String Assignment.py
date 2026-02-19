# Page 52==== Exercise 6.11 ==== no.1 -- a-k
# Ask user for input
text = input("Enter a string: ")

# (a) Total number of characters
print("(a) Total characters:", len(text))

# (b) String repeated 10 times
print("(b) Repeated 10 times:", text * 10)

# (c) First character (index starts at 0)
if len(text) > 0:
    print("(c) First character:", text[0])
else:
    print("(c) String is empty")

# (d) First three characters
print("(d) First three characters:", text[:3])

# (e) Last three characters
print("(e) Last three characters:", text[-3:])

# (f) String backwards
print("(f) Backwards:", text[::-1])

# (g) Seventh character if long enough
if len(text) >= 7:
    print("(g) Seventh character:", text[6])
else:
    print("(g) String is not long enough")

# (h) Remove first and last characters
if len(text) > 2:
    print("(h) Without first and last:", text[1:-1])
else:
    print("(h) String too short")

# (i) All caps
print("(i) All caps:", text.upper())

# (j) Replace every 'a' with 'e'
print("(j) Replace 'a' with 'e':", text.replace('a', 'e'))

# (k) Replace every letter with a space
print("(k) Letters replaced by spaces:", " " * len(text))