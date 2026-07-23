"""Create a class Student.

Private:

__marks

Create:

get_marks()

Return the marks."""


class student:
    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

s1 = student(202)

print(s1.get_marks())