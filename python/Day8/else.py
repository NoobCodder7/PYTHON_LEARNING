try:

    num = int(input("Number: "))

    print(10 / num)

except ZeroDivisionError:

    print("Division by zero.")

else:

    print("Everything worked!")