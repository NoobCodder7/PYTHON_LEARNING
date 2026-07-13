#16. Build a simple calculator using `if-elif-else`.

num1 = int(input("Enter a number "))
operator = input("Enter operator (+, -, *, /): ")
num2 = int(input("Enter a number "))

if operator == "+":
    print("Result =", num1 + num2)

elif operator == "-":
    print("Result =", num1 - num2)

elif operator == "*":
    print("Result =", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Error! Division by zero is not allowed.")

else:
    print("Invalid operator! Please enter +, -, *, or /.")