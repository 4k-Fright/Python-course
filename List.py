
# List is similar to variables only that they can contain multiple values. OR contain as many variables
# List can be iterated over in a very simple manner. Here's an example on how to build a list

mylist = [1,2,3]     # OR use mylist.append(1) to add
print(mylist[0])  # prints 1
print(mylist[1])  #prints 2
print(mylist[2])  # prints 3


# Here we are iterating our list using loop, it might seem unclear but will be clear soon enough
# prints out 1,2,3
for x in mylist:
    print(x)


# Accessing an index which does not exist generates an exception (an error).

numbers = [1,2,3]
# print(numbers[10])


# List by accepting its values from user
L = eval(input('Enter a list: '))
print('the first element is', L[0])
print(L)


#===============================================


# List with values
L = [5,7,9]
print(L)

for i in range(len(L)):
    print(L[i])



#================================================


L = [1, 2.718, 'abc', [5,6,7]]
print(L)

for i in range(len(L)):
    print(L[i])



# Using if-in condition with list
L = [1,2,3,3,4,5]
if 2 in L:
    print('Your list contain the number 2.')
else:
    print('Your list doesn\'t contain the number 2.')

if 0 not in L:
    print('Your list has no zeroes.')
else:
    print('Your list has no zeroes.')


#==================================================

L = [1, 2.718, 'abc', [5,6,7]]
print(L[:3])

#===================================================



print([7,8] + [3,4,5])
print([7,8] * 3)
print([0] * 5)

#====================================================


L = [1,2,3,4,5]
for i in range(len(L)):
    print(L[i])
    # or this way
for item in L:
    print(item)


#=================================================================
# List Methods

L = [1,2,3,4,5,6]
mysum = sum(L)
print('the sum of the list is', mysum)
mylen = len(L)
print('the length of the list is', mylen)
mymin = min(L)
print('the minimum value of the list is', mymin)
mymax = max(L)
print('the maximum value of the list is', mymax)

average = sum(L)/len(L)
print('the average value of the list is', average)

#==================================================================



# Function of the list.  How to use append function

L = [3,9,5,6,7]
L.append(2)
print(L)

# How to use sort function

L = [3,9,5,6,7]
L.sort()
print(L)

# How to use count function

L = [3,9,3,6,3]
x = L.count(3)
print(x)

# How to use index function

L = [3,9,5,6,7]
x  = L.index(9)
print(x)

# How to use a reverse function

L = [3,9,5,6,7]
L.reverse()
print(L)

# How to use remove function

L = [3,9,5,6,7]
L.remove(5)
print(L)

# How to use pop function
L = [3,9,5,6,7]
x = L.pop(2)
print(x)
print(L)

# How to use insert function
L = [3,9,5,6,7]
L.insert(1,8)
print(L)


#======================================================================


# How to copy a list

L = [3,9,5,6,7]
M = L[:]
print(M)

# How to change lists by replacing

L = [6,7,8]
L[1] = 9
print(L)

# How to insert lists without replacing

L = [6,7,8]
L.insert(1,4)
print(L)

# How to delete second item in the list

L = [6,7,8]
del L[1]
print(L)

# How to delete first two items in the list

L = [6,7,8]
del L[:2]
print(L)




# Write a program that generates a list L of 10 random numbers between

from random import randint
L = []
for i in range(10):
    L.append(randint(1,100))
print(L)


# Replace each element in a list L with its square
L = [1,2,3]
for i in range(len(L)):
    L[i] = L[i] ** 2
print(L)




# Count how many items in a list L are greater than 50.

L = [50,7,89,34,67,98,2,4,6,9,1]
count = 0
for item in L:
    if item > 50:
        print(item)
        count = count + 1
print('Total is :', count)


#=====================================================================

L = [1,2,3,2,4,4,4,5,5,6,7,7,8,9,10,11,12,13,14,15]
frequencies = []
for i in range(1, 16):
    frequencies.append(L.count(i))
print(frequencies)

#=====================================================================


scores = [5,3,7,8,9,6,34,2,80]
scores.sort()
print(scores)
print('Two smallest', scores[0], scores[1])
print('Two largest', scores[-1], scores[-2])

#=====================================================================

# Here is program to play a simple quiz game.

num_right = 0
# Question 1
print('What is the capital of france', end = ' ')
guess = input()
if guess.lower() == 'paris':
    print('Correct!')
    num_right += 1
else:
    print('Wrong!, Answer is Paris')
    print('You have', num_right, 'out of 1 right')

# Question 2
print('Which state has only one neighbor?', end = '')
guess = input()
if guess.lower() == 'maine':
    print('Correct!')
    num_right += 1
else:
    print('Wrong!, Answer is Maine')
    print('You have', num_right, 'out of 2 right')

print("You got ", num_right, "correctly")




#=========================================================================================


questions = ['What is the capital of France?', 'Which state has only one neighbor']
answers = ['Paris', 'Maine']
num_right = 0
for i in range(len(questions)):
    guess = input(questions[i])
    if guess.lower() == answers[i].lower():
        print('Correct!')
        num_right = num_right + 1
    else:
        print('Wrong!, Answer is ' + answers[i])
        print('You have', num_right, 'out of', i + 1, 'right')

#===========================================================================================