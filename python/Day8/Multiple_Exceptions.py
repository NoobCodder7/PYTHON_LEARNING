try:

    num = int(input("Number: "))

    print(10 / num)

except ValueError:
    print("Enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")