#1. Create a calculator using functions.

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b 

def div(a, b):
    if b == 0:
      return "Error! Division by zero is not allowed."
    return a / b



print("---------------------------------------------------------------Simple Calculator---------------------------------------------------------------")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter Your Choice (1-4)"))

a = float(input("Enter value of a "))
b = float(input("Enter value of b "))

if choice == 1:
    print("Result: ", add(a,b))
elif choice == 2:
        print("Result: ", add(a,b))
elif choice == 2:
        print("Result: ", sub(a,b))

elif choice == 3:
        print("Result: ", mul(a,b))

elif choice == 4:
        print("Result: ", div(a,b))
        
else:
     print("entered choice is invalid")



