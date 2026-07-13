#11. Calculate grades based on marks.

mark1 = float((input("Enter marks of subject 1")))
mark2 = float((input("Enter marks of subject 2")))
mark3 = float((input("Enter marks of subject 3")))
mark4 = float((input("Enter marks of subject 4")))
mark5 = float((input("Enter marks of subject 5")))

marks = mark1+mark2+mark3+mark4+mark5

if marks < 0 or marks > 500:
    print("Invalid marks! Please enter marks between 0 and 500.")
elif marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F (Fail)")