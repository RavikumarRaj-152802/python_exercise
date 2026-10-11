# Q.7. Write a program to create a dictionary and demonstrate dictionary methods and iteration.

# Creating a dictionary
student = {
    "name": "Rahul",
    "age": 18,
    "course": "Python",
    "marks": 85
}

print("Original Dictionary:", student)

# Accessing values
print("Student Name:", student["name"])
print("Student Age:", student.get("age"))

# Dictionary methods
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Adding and updating elements
student["city"] = "Ahmedabad"
student["marks"] = 90
print("After Adding and Updating:", student)

# Removing an element

student.pop("age")
print("After Removing Age:", student)

# Iterating through the dictionary
print("\nDictionary Elements:")

for key, value in student.items():
    print(key, ":", value)