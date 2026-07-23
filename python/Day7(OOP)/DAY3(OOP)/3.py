"""Q1

Create a class Student.

Public variable: name
Store your name.
Print it."""


class Student:
    def __init__(self ,name):
        self.name = name

s1 = Student("Viraj")
print(s1.name)


"""Q2

Create a class Car.

Public variables:
brand
color

Print both."""



class car:
    def __init__(self, brand, colour):

        self.brand = brand 
        self.colour = colour

c1 = car("BMW" , "RED")

print(c1.brand)
print(c1.colour)


"""Create 3 Student objects with different names and ages.

Print all their details."""


class students:
    def __init__(self, name ,age):
        self.name = name
        self.age = age


s1 = students("viraj", 20)
s2 = students("rahul", 42)
s3 = students("frank", 20)


print("--------------------Student Detail--------------------" )
print(f"the name of the student is {s1.name} and age is  {s1.age}")
print(f"the name of the student is {s2.name} and age is  {s2.age}")
print(f"the name of the student is {s3.name} and age is  {s3.age}")



"""Create a class Student.

Store:

name (public)
_marks (protected)

Print both."""


class student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks


s1 = student("raj" , 23)
print(s1.name)
print(s1._marks)



