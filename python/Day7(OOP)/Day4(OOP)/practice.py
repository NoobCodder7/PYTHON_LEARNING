"""-----------------------------------------📝 Practice Questions"-------------------------------------------"""


"""Q1
Create a class Animal.
Create a method:"""

class animal:
    def eat(self):
        print("eating")

a1 = animal()
a1.eat()


"""Q2
Create a child class Dog.
Inherit from Animal.
Call eat()."""

class animal:
    def eat(self):
        print("Eating")
class dog(animal):
    pass
d1 = dog()
d1.eat()


"""Create a class Vehicle.
Method:
start()
Create child class Car.
Call start()."""


class vehicle:
    def start(self):
        print("Vroom Vroom")
class car(vehicle):
    pass
c1 = car()
c1.start()




"""Q3

Create parent class Animal.
Method:
eat()
Create child class Dog.
Method:
bark()
Call both methods."""

class animal:
    def eat(self):
        print("Eating")
class dog(animal):
    def barks(self):
        print("Bhow Bhow")

d = dog()
d.eat()
d.barks()



