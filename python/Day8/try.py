try:
    a = 10
    b = 0

    print(a / b)

except:
    print("Cannot divide by zero.")

print("Done")


try:
    print(10 / 0)

except ZeroDivisionError:
    print("Division by zero is not allowed.")