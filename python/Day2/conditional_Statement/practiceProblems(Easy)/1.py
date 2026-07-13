#1. Check whether a number is positive or negative.

n = int(input("Enter a number"))

if n > 0:
    print("Entered number is positive")
elif n < 0:
    print("Entered number is negative")

else:
    print("Number is zero")