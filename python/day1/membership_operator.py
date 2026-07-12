# Membership Operators in Python
# Used to check whether a value exists in a sequence
# such as a string, list, tuple, set, or dictionary.

# in      Returns True if the value is present.
# not in  Returns True if the value is not present.


fruits = ["apple", "banana", "mango"]

print("apple" in fruits)       # True
print("grapes" in fruits)      # False
print("grapes" not in fruits)  # True

text = "Python"

print("P" in text)             # True
print("z" not in text)         # True