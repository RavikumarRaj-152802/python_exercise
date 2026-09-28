'''
    Q(1) a college want to seperate its student result calculations 
    from main application. creat a modue named result untils.py 
    containing function to calculate total marks, percentage, and 
    grade for a students. import this module into main.py and 
    generate a formatted result for a student. demonstrate use of 
    both import module and from module import functio approaches, 
    also explain its concept in short
'''
# result_utils.py

def calculate_total(marks):
    return sum(marks)


def calculate_percentage(marks):
    total = calculate_total(marks)
    return total / len(marks)


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"