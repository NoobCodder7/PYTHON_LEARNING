"""Question 1

Create a class called Car.
Store:
Brand
Color
Print both."""


class car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

C1 = car("BMW", "Red")
print("The brand of the car is:", C1.brand)
print("The color of the car is:", C1.color)




"""Question 2
Create a class Book.
Store:

Title
Author

Create two books."""


class book:
    def __init__(self, name , author):
        self.name = name
        self.author = author

B1 = book("Book A" ,"A")
B2 = book("Book B" ,"B")


print(f"The name of the book is {B1.name} and author is {B1.author}")
print(f"The name of the book is {B2.name} and author is {B2.author}")





"""Create a class Laptop.
Store:

Brand
Price

Print the details."""



class laptop:
    def __init__(self, name , price):
        self.name = name
        self.price = price

L1 = laptop("ASUS" , "59k")      
L2 = laptop("APPLE" , "100k") 

print(f"The name of the laptop is {L1.name} and price is {L1.price}")
print(f"The name of the laptop is {L2.name} and price is {L2.price}")

print("\n")

"""
Question 4
Create a class Employee.
Store:

Name
Salary
Department

Create three employees."""


class Employees:
    def __init__(self, Name , Salary , Department):
        self.Name = Name
        self.Salary = Salary
        self.Department = Department

E1 = Employees("Viraj" , "$400000" , "IT")
E2 = Employees("Rahul" , "$4000" , "Marketing")
E3 = Employees("Frank" , "$400000" , "IT")



print(f"The name of the Employee is {E1.Name} and Salary is {E1.Salary} and Department is {E1.Department}\n")
print(f"The name of the Employee is {E2.Name} and Salary is {E2.Salary} and Department is {E2.Department}\n")
print(f"The name of the Employee is {E3.Name} and Salary is {E3.Salary} and Department is {E3.Department}\n")



"""Question 9

Create a class BankAccount.
Store

Account Holder
Account Number
Balance

Print all account details."""


class BankAccount:
    def __init__(self, Aname, Anumber, Atype):
        self.Aname = Aname
        self.Anumber = Anumber
        self.Atype = Atype

    def ACC_Details(self):
        print("------------------------------------------------ Account Details ------------------------------------------------")
        print(f"The name of account holder is {self.Aname}")
        print(f"The account number is {self.Anumber}")
        print(f"The account type is {self.Atype}")

acc1 = BankAccount("Viraj", 1234567890, "Savings")
acc2 = BankAccount("frank", 2933422344, "Current")
acc3 = BankAccount("Sujal", 9233291313, "Joint")

acc1.ACC_Details()
acc2.ACC_Details()
acc3.ACC_Details()