# Q.4. Write a program to demonstrate string operations including slicing formatting and built-in string functions.

s = "Hello Python"

# String slicing

print("Original String:", s)
print("First five characters:", s[0:5])

print("Characters from index 6:", s[6:])
print("Reverse String:", s[::-1])

# String formatting

name = "Rahul"
age = 18

print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")

# Built-in string functions

text = "  python programming  "
print("Uppercase:", text.upper())

print("Lowercase:", text.lower())
print("Title Case:", text.title())

print("Length:", len(text))
print("After removing spaces:", text.strip())

print("Replace:", text.replace("python", "Java"))
print("Count of 'm':", text.count("m"))
print("Find 'programming':", text.find("programming"))