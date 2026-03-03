#  3
for i in range(1, 5):
    print("*" * i)


#  4
result = (512 - 282) / (47 * 48 + 5)
print(result)


#  5
num = int(input("Enter a number: "))
print("The square of", num, "is", num ** 2, ".", sep=" ")


#  6
x = int(input("Enter a number: "))
print(x, 2*x, 3*x, 4*x, 5*x, sep="---")


#  7
kilogram = float(input("Enter a weight in kilogram: "))
pounds = kilogram * 2.2
print("converting to pounds", pounds)


#  8
no1 = int(input("Enter first number: "))
no2 = int(input("Enter second number: "))
no3 = int(input("Enter third number: "))

total = no1 + no2 + no3
average = total / 3

print("total is: ", total)
print("average is: ", average)


#  9
price = float(input("Enter a price: "))
percent = float(input("Enter a percent: "))
tip = price * (percent / 100)
bill = price + tip
print("tip is: ", tip)
print("bill is: ", bill)