# Q.5. Write a program to create and manipulate lists using indexing slicing and list comprehensions.

# Create a list

numbers = [10, 20, 30, 40, 50]
print("Original List:", numbers)

# List indexing

print("First Element:", numbers[0])
print("Last Element:", numbers[-1])

# List slicing

print("First Three Elements:", numbers[0:3])
print("Elements from Index 2:", numbers[2:])
print("Reversed List:", numbers[::-1])

# Manipulating a list

numbers.append(60)
print("After Append:", numbers)

numbers.remove(30)
print("After Remove:", numbers)

numbers[0] = 100
print("After Updating:", numbers)

# List comprehension

squares = [x * x for x in range(1, 6)]
print("Squares:", squares)

# List comprehension with condition

even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("Even Numbers:", even_numbers)