#12. Find the smallest of three numbers.
num1 = int(input("Enter number"))
num2 = int(input("Enter number"))
num3 = int(input("Enter number"))

if num1>=num2 and num1>=num3:
    print("num 1 is the biggest")
elif num2>=num1 and num2>=num3:
    print("num 2 is the biggest")
else:
    print("Num 3 is biggeset")
