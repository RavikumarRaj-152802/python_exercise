#Q.6 Write a Python program to enter two nos. and find maximum out of it.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    maximum = a
else:
    maximum = b

print("Maximum number =", maximum)