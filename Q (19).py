# Q.(19)Write a Python Program to enter 10 nos. and find max1,max2,max3 and min1,min2 and min3

numbers = []

for i in range(10):
    n = int(input("Enter number: "))
    numbers.append(n)

numbers.sort()

print("Maximum 1 =", numbers[-1])
print("Maximum 2 =", numbers[-2])
print("Maximum 3 =", numbers[-3])

print("Minimum 1 =", numbers[0])
print("Minimum 2 =", numbers[1])
print("Minimum 3 =", numbers[2])