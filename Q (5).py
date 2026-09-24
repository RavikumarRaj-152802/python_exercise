#Q.5 Write a Python Program to enter marks of 3 subjects and find total, percentage, result and class.

marks1 = float(input("Enter marks of Subject 1: "))
marks2 = float(input("Enter marks of Subject 2: "))
marks3 = float(input("Enter marks of Subject 3: "))

total = marks1 + marks2 + marks3
percentage = total / 3

# Result
if marks1 >= 35 and marks2 >= 35 and marks3 >= 35:
    result = "PASS"

    # Class
    if percentage >= 60:
        class_name = "First Class"

    elif percentage >= 50:
        class_name = "Second Class"
        
    elif percentage >= 35:
        class_name = "Third Class"
else:
    result = "FAIL"
    class_name = "No Class"

print("\nTotal Marks =", total)
print("Percentage =", percentage, "%")
print("Result =", result)
print("Class =", class_name)