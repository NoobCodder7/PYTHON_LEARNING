#10. Check whether a number is a multiple of both 3 and 5.

num = float(input("Enter a number "))

if (num % 3 ==0) and (num % 5 ==0):
    print("Entered number is multiple of 3 and 5 ")
else:
    print("Entered number is not a multiple of 3 and 5 ")
