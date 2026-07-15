#4. Student Report Card Generator.
# 4. Student Report Card Generator

name = input("Enter Student Name: ")

maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

total = maths + science + english
percentage = total / 3

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n----- REPORT CARD -----")
print("Student Name :", name)
print("Maths        :", maths)
print("Science      :", science)
print("English      :", english)
print("Total Marks  :", total)
print("Percentage   :", percentage, "%")
print("Grade        :", grade)