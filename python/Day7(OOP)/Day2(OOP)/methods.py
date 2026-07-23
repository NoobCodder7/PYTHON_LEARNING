class Student:
    def __init__(self, name, age, number):
        self.name = name
        self.age = age
        self.number = number

        def intro(self):
            print("hello my name is ", self.name)
            print("hello my name is ", self.age)
            print("hello my name is ", self.number)


S1 = Student("Viraj" , 20, 9540234743)
S2 = Student("Frank", 20, 9230495345)

print("-------------------------------------DETAILS OF STUDENT 1-------------------------------------")
print("Name = ", S1.name)
print("age = ", S1.age)
print("Number = ", S1.number)

print("-------------------------------------DETAILS OF STUDENT 2-------------------------------------")
print("Name = ", S2.name)
print("age = ", S2.age)
print("Number = ", S2.number)