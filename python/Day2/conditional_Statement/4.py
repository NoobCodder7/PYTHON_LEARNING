# Banking System Menu

balance = 10000

while True:
    print("\n===== BANKING SYSTEM =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        print(f"Your current balance is ₹{balance}")

    elif choice == 2:
        amount = float(input("Enter deposit amount: ₹"))

        if amount > 0:
            balance += amount
            print(f"₹{amount} deposited successfully.")
            print(f"Updated Balance: ₹{balance}")
        else:
            print("Invalid deposit amount.")

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            print(f"Remaining Balance: ₹{balance}")

    elif choice == 4:
        print("Thank you for using our Banking System!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")