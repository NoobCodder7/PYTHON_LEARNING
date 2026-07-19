# 16. Create a function to count vowels in a string.

def count_vowels(text):
    count = 0

    vowels = "aeiouAEIOU"

    for ch in text:
        if ch in vowels:
            count += 1

    return count


# Main Program
string = input("Enter a string: ")

result = count_vowels(string)

print("Number of vowels:", result)