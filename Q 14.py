# (14) Write a Python Program to enter a no. and check it is Armstrong or not? 

n = int(input("Enter a number: "))

original = n
digits = len(str(n))
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit ** digits
    n = n // 10

if original == sum:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")