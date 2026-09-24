#Q (8).Write a Python Program to enter 10 Nos. and find sum and average of it

sum = 0

for i in range(1, 11):
    num = float(input("Enter number " + str(i) + ": "))

sum = sum + num
average = sum / 10

print("Sum =", sum)
print("Average =", average)