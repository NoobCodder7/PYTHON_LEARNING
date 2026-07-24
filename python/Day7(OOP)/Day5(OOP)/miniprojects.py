"""Project 1 — Animal Sounds

Parent

Animal

Children

Dog

Cat

Cow

Lion

Each overrides

sound()"""


class animal:
    def sound(self):
        print("Animals make the sound")
class dog(animal):
    def sound(self):
        print("Bhow Bhow")
class cat(animal):
    def sound(self):
        print("mew mew")
class lion(animal):
    def sound(self):
        print("roarrrrrrrr")
class cow(animal):
    def sound(self):
        print("MOooooooo MOooooooooooooooo")


d = dog()
c = cat()
l = lion()
co = cow()


d.sound()
c.sound()
co.sound()
l.sound()