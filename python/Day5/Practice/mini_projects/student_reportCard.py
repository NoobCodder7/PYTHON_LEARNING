#4. Create a student report card generator using functions.
# Student Report Card Generator Using Functions

def calculate_total(marks):
    return sum(marks)


def calculate_percentage(total, subjects):
    return total / subjects


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
    elif percentage >= 35:
        return "Pass"
    else:
        return "Fail"


def display_report(name, marks, total, percentage, grade):
    print("\n========== STUDENT REPORT CARD ==========")
    print("Student Name :", name)
    print("Marks :", marks)
    print("Total Marks :", total)
    print("Percentage :", round(percentage, 2), "%")
    print("Grade :", grade)
    print("=========================================")


# Main Program
name = input("Enter student name: ")

subjects = int(input("Enter number of subjects: "))

marks = []

for i in range(subjects):
    mark = float(input(f"Enter marks for Subject {i + 1}: "))
    marks.append(mark)

total = calculate_total(marks)
percentage = calculate_percentage(total, subjects)
grade = calculate_grade(percentage)

display_report(name, marks, total, percentage, grade)