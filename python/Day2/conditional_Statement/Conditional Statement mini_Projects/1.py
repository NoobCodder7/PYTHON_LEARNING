# 1. ATM Menu using if-elif-else

Account_number = 9429096969
Account_Type = "Savings"
balance = 200000

option = input("Enter operation (Withdrawal, Deposit, Check_Balance): ")

if option == "Withdrawal":
    amount = int(input("Enter amount to withdraw: "))

    if amount > balance:
        print("Insufficient Balance!")
    else:
        balance = balance - amount
        print("Withdrawal Successful!")
        print("Remaining Balance =", balance)

elif option == "Deposit":
    amount = int(input("Enter amount to deposit: "))
    balance = balance + amount
    print("Deposit Successful!")
    print("Updated Balance =", balance)

elif option == "Check_Balance":
    print("Your Account Balance is:", balance)

else:
    print("Invalid Option!")