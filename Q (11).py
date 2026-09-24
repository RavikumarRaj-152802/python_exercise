#Q.11 Write a Python Program to enter a no. and find sum of its digits.

n = int(input("Enter a number: "))

sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10

print("Sum of digits =", sum)