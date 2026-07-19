# 20. Create a function using `**kwargs` to print student details.

def student_details(**kwargs):
    print("Student Details:")

    for key, value in kwargs.items():
        print(key, ":", value)


# Main Program
student_details(
    Name="Viraj",
    Age=20,
    Course="B.Tech CSE",
    College="ABC College",
    City="Surat"
)