# Q (15)Write a Python Program to enter a no. and check it is prime or not?

n = int(input("Enter a number: "))

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1

if count == 2:
    print("Number is Prime")
else:
    print("Number is not Prime")