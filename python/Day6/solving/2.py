text = "Although learning Python is fun, my Python professor told me that Python code must be written carefully to become a true Python expert."

with open("r.txt", "r") as file:
    data = file.read()

python_count = data.count("Python")

vowels = 0
upper = 0
lower = 0
digits = 0
spaces = 0

for ch in data:
    if ch.lower() in "aeiou":
        vowels += 1

    if ch.isupper():
        upper += 1

    if ch.islower():
        lower += 1

    if ch.isdigit():
        digits += 1

    if ch == " ":
        spaces += 1

print("Python appears:", python_count)
print("Vowels:", vowels)
print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digits)
print("Spaces:", spaces)
