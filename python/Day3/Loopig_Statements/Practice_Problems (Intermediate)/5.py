#15. Count the vowels in a string.

string = 'Hello'
vovel = 0
for char in string:
    if char.lower() in "aeiou":
        vovel += 1
print("Number of vowels =", vovel)