"""🟠 Hard Level (Private Variables)"""


"""Q11
Create a class Student.
Store:

__password"""

class Bank:
    def __init__(self, balance):
        self.__balance = balance


# Create object
b1 = Bank(5000)

# Try accessing private attribute directly
print(b1.__balance)