#17. Create a function to reverse a string.


def reverse_string(text):
    reverse = ""

    for ch in text:
        reverse = ch + reverse

    return reverse


# Main Program
string = input("Enter a string: ")

result = reverse_string(string)

print("Reversed String:", result)