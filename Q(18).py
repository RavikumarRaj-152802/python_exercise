# Q.(18)Write a Python Program to enter 10 nos. and sort them in ascending order

numbers = []

for i in range(10):
    n = int(input("Enter number: "))
    numbers.append(n)

numbers.sort()

print("Numbers in ascending order:")

for n in numbers:
    print(n, end=" ")