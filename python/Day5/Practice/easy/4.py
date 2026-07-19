#9. Create a function to check whether a number is even or odd.

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


number = int(input("Enter a number: "))
result = check_even_odd(number)
print(f"{number} is {result}.")