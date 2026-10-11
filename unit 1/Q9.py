# Q.9. Write a program to define and use user-defined functions with different types of arguments.

# Function with no arguments

def greet():
    print("Hello, Welcome to Python!")

# Function with positional arguments

def add(a, b):
    print("Sum:", a + b)

# Function with default arguments

def student(name, age=18):
    print("Name:", name)
    print("Age:", age)

# Function with keyword arguments

def display(name, course):
    print("Name:", name)
    print("Course:", course)

# Function with variable-length arguments

def total(*numbers):
    print("Total:", sum(numbers))

# Calling the functions
greet()
add(10, 20)
student("Rahul")
student("Amit", 21)
display(course="Python", name="Neha")
total(10, 20, 30, 40)