"""⭐ Major Project — Hospital Management System"""

class person:
    def __init__(self, name ,age):
        self.name = name
        self.age = age 

    def display(self):
        print(f"Name = {self.name}")
        print(f"age = {self.age}")

    def work(self):
        print("the person is wokring")

class doctor(person):
    def work(self):
        print(f"Dr.{self.name} is treating patient")

class Nurse(person):
    def work(self):
        print(f"{self.name} is assisting the doctor.")


class Patient(person):
    def work(self):
        print(f"{self.name} is receiving treatment.")


class Receptionist(person):
    def work(self):
        print(f"{self.name} is managing appointments.")

d1 = doctor("Viraj", 30)
n1 = Nurse("Anjali", 28)
p1 = Patient("Rahul", 22)
r1 = Receptionist("Priya", 25)

hospital = [d1, n1, p1, r1]


for person in hospital:
    print("-"*40)
    person.display()
    person.work()