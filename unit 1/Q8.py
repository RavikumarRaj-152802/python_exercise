# Q.8. Write a program to explain mutable and immutable objects in Python.

# Mutable object (List)

list1 = [10, 20, 30]
print("Original List:", list1)

list1[0] = 100
print("Modified List:", list1)

# Immutable object (Tuple)

tuple1 = (10, 20, 30)
print("\nOriginal Tuple:", tuple1)

# Creating a new tuple instead of modifying it

tuple1 = (100, 20, 30)
print("New Tuple:", tuple1)

# Immutable object (String)

str1 = "Hello"
print("\nOriginal String:", str1)

str1 = "Python"
print("New String:", str1)