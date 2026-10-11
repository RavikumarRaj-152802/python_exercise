# Q.10.Write a program to demonstrate recursion using factorial or Fibonacci series.

# Program to find factorial using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Taking input from the user
num = int(input("Enter a number: "))

# Displaying the result

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial of", num, "is", factorial(num))