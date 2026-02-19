# List Exercise 7.7 1- 10
#============================================================================================================================================
#   NO> 1. List of integers (user input)
nums = list(map(int, input("Enter integers separated by spaces: ").split()))

# (a)
print("(a) Total items:", len(nums))

# (b)
print("(b) Last item:", nums[-1] if nums else "List is empty")

# (c)
print("(c) Reversed list:", nums[::-1])

# (d)
print("(d) Contains 5:", "Yes" if 5 in nums else "No")

# (e)
print("(e) Number of fives:", nums.count(5))

# (f)
if len(nums) > 2:
    trimmed = nums[1:-1]
    trimmed.sort()
    print("(f) Sorted without first & last:", trimmed)
else:
    print("(f) List too short")

# (g)
print("(g) Less than 5:", sum(1 for n in nums if n < 5))




#====================================================================================================
#   NO> 2. Random numbers (1–100)
import random

nums = [random.randint(1, 100) for _ in range(20)]

# (a)
print("(a) List:", nums)

# (b)
print("(b) Average:", sum(nums) / len(nums))

# (c)
print("(c) Largest:", max(nums))
print("    Smallest:", min(nums))

# (d)
sorted_nums = sorted(nums)
print("(d) Second smallest:", sorted_nums[1])
print("    Second largest:", sorted_nums[-2])
print("    Even numbers:", sum(1 for n in nums if n % 2 == 0))




#=======================================================================================================
#   NO> 3. Start with [8,9,10]
lst = [8, 9, 10]

# (a)
lst[1] = 17

# (b)
lst.extend([4, 5, 6])

# (c)
lst.pop(0)

# (d)
lst.sort()

# (e)
lst = lst * 2

# (f)
lst.insert(3, 25)

print("Final list:", lst)




#====================================================================================================================
#   NO> 4. Replace values > 10 with 10
nums = list(map(int, input("Enter numbers between 1 and 12: ").split()))
nums = [10 if n > 10 else n for n in nums]
print(nums)




#==========================================================================================================
#   NO> 5. Remove first character from each string
words = input("Enter strings separated by spaces: ").split()
new_list = [w[1:] for w in words if len(w) > 0]
print(new_list)




#===========================================================================================================
#   NO> 6. Lists using a for loop
# (a)
a = []
for i in range(50):
    a.append(i)

# (b)
b = []
for i in range(51):
    b.append(i * i)

# (c)
c = []
for i in range(26):
    c.append(chr(97 + i) * (i + 1))

print(a)
print(b)
print(c)




#=============================================================================================
#    NO> 7. Add two lists element-wise
L = list(map(int, input("Enter list L: ").split()))
M = list(map(int, input("Enter list M: ").split()))

result = [L[i] + M[i] for i in range(len(L))]
print(result)




#=========================================================================================================
#    NO> 8. Factors of an integer
n = int(input("Enter an integer: "))
factors = [i for i in range(1, n + 1) if n % i == 0]
print(factors)