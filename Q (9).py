#Q (9). Write a Python Program to enter 10 Nos. and find Maximum out of it without using array.

num = float(input("Enter number 1: "))
maximum = num

for i in range(2, 11):
    num = float(input("Enter number " + str(i) + ": "))

    if num > maximum:
        maximum = num

print("Maximum number =", maximum)