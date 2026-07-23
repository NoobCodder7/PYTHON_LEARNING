"""🟣 Setter Method Practice
Q21

Create a class Student.

Private:

__marks

Create:

set_marks()

Only allow marks between 0 and 100."""


class student:
    def __init__(self, marks ):
        self.__marks = marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            print("Marks updated successfully.")
        else:
            print("Invalid marks! Marks should be between 0 and 100.")

    def get_marks(self):
        return self.__marks


# Create object
s1 = student(85)

print("Current Marks:", s1.get_marks())

s1.set_marks(95)      # Valid
print("Updated Marks:", s1.get_marks())

s1.set_marks(120)     # Invalid
print("Final Marks:", s1.get_marks())