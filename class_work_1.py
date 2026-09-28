'''
    Q(1) a college want to seperate its student result calculations 
    from main application. creat a modue named result untils.py 
    containing function to calculate total marks, percentage, and 
    grade for a students. import this module into main.py and 
    generate a formatted result for a student. demonstrate use of 
    both import module and from module import functio approaches, 
    also explain its concept in short
'''
# main.py

# Approach 1: import module
import result_utils

# Approach 2: from module import functions
from result_utils import calculate_total, calculate_percentage, calculate_grade

# Student details
name = "Ravi Kumar"
marks = [85, 90, 78, 88, 92]

# Using imported module
total1 = result_utils.calculate_total(marks)
percentage1 = result_utils.calculate_percentage(marks)

# Using directly imported functions
grade = calculate_grade(percentage1)

# Formatted result
print("========== STUDENT RESULT ==========")
print("Name       :", name)
print("Marks      :", marks)
print("Total      :", total1)
print("Percentage :", round(percentage1, 2), "%")
print("Grade      :", grade)
print("====================================")