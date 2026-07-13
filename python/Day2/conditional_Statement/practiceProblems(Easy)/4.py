#4. Find the largest of three numbers.

num1 = float(input("Enter a number"))
num2 = float(input("Enter a number"))
num3 = float(input("Enter a number"))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Displaying the result
print(f"The largest number is: {largest}")