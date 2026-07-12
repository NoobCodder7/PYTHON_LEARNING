# Identity Operators in Python
# Used to check whether two variables refer to the same object in memory.

# is      Returns True if both variables refer to the same object.
# is not  Returns True if both variables refer to different objects.

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)       # True (same object)
print(a is c)       # False (different objects)
print(a == c)       # True (same values)
print(a is not c)   # True (different objects)