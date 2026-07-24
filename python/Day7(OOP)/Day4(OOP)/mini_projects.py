"""Project 1

Create an Animal Management System.

Parent:
eat()
sleep()

Children:

Dog
Cat
Lion

Each child has its own method."""



class animal:
    def eat (self):
        print("eating")
    def sleep(self):
        print("sleeping")
class dog(animal):
    def bark(self):
        print("Bhow Bhow")
class cat(animal):
    def mew(self):
        print("mew mew")
class lion(animal):
    def roar(self):
        print("roaaaaaa roaaaaaaaa")

d1 = dog()
c1 = cat()
l1 = lion()

d1.bark()
d1.sleep()
c1.mew()
c1.sleep()
l1.roar()
l1.sleep()




"""Project 3

Create a School System.

Parent:
Person

Children:

Student
Teacher

Each child has its own method"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    def study(self):
        print(f"{self.name} is studying.")


class Teacher(Person):
    def teach(self):
        print(f"{self.name} is teaching.")


# Student Object
s1 = Student("Viraj", 20)
print("----- Student -----")
s1.display()
s1.study()

print()

# Teacher Object
t1 = Teacher("Mr. Sharma", 35)
print("----- Teacher -----")
t1.display()
t1.teach()



"""Create a Banking System.

Parent:

Account

Children:

SavingsAccount
CurrentAccount

Each child should have one unique method."""

class Account:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def display_details(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ₹{self.balance}")


class SavingsAccount(Account):
    def add_interest(self):
        interest = self.balance * 0.05
        self.balance += interest
        print(f"Interest Added: ₹{interest}")
        print(f"New Balance: ₹{self.balance}")


class CurrentAccount(Account):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} Withdrawn Successfully")
            print(f"Remaining Balance: ₹{self.balance}")
        else:
            print("Insufficient Balance")


# Savings Account Object
s1 = SavingsAccount("Viraj", 10000)
print("----- Savings Account -----")
s1.display_details()
s1.add_interest()

print()

# Current Account Object
c1 = CurrentAccount("Rahul", 15000)
print("----- Current Account -----")
c1.display_details()
c1.withdraw(3000)