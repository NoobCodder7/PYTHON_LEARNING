# 1. ZeroDivisionError
try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero.")

#2. ValueError
try:
    age = int(input("Age: "))

except ValueError:
    print("Please enter numbers only.")

#3. IndexError
numbers = [10,20,30]

try:
    print(numbers[5])

except IndexError:
    print("Index does not exist.")

#4. KeyError

student = {
    "name":"Viraj"
}

try:
    print(student["age"])

except KeyError:
    print("Key not found.")

#5. FileNotFoundError

try:
    with open("abc.txt","r") as file:
        print(file.read())

except FileNotFoundError:
    print("File does not exist.")