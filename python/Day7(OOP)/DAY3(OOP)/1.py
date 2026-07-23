class student:
    def __init__(self, name, marks, password):
        self.name = name
        self._marks = marks
        self.__password = password
    def get_bal(self):
        return self.__password

s1 = student("Viraj", 80, "Virja1929")

print(s1.name)
print(s1._marks)
print(s1.get_bal())