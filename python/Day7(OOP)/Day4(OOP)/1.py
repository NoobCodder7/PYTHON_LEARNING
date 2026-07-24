class dog:
    def eat(self):
        print("eating")
class cat:
    def eat(self):
        print("eating")


"""We're writing the same method again and again.
Now imagine 100 animals.
That would be a lot of repeated code."""

"""Insted we will use the concept of inheritance """

class animal:
    def eat(self):
        print("Eating")
class dog(animal):
    pass
class cat(animal):
    pass


d = dog()
d.eat()


""" Child Class with Its Own Method """


class animal:
    def eat(self):
        print("Eating")
class dog(animal):
    def bark(self):print("Bhow Bhow")

class cat(animal):
    pass


d = dog()
d.eat()
d.bark()


"""The super() Function"""

class Animal:

    def __init__(self):
        print("Animal Created")


class Dog(Animal):

    def __init__(self):
        super().__init__()
        print("Dog Created")


dog = Dog()



"""Method Overriding"""

class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):
        print("Bark")


dog = Dog()

dog.sound()