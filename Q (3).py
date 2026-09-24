#Q3. Write a Python Program to enter Principle Amt., Rate of Interest and No. of Years and find Simple and Compound Interest.

P = float(input("Enter Principal Amount: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Number of Years: "))

# Simple Interest
SI = (P * R * T) / 100

# Compound Interest
CI = P * (1 + R / 100) ** T - P

print("Simple Interest =", SI)
print("Compound Interest =", CI)