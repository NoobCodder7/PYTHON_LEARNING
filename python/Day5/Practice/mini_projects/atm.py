# ATM Program Using Functions

balance = 10000
pin = "1234"


def check_balance():
    print("Your current balance is:", balance)


def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print("Deposit successful!")
        print("Updated balance:", balance)
    else:
        print("Invalid amount!")


def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount <= 0:
        print("Invalid amount!")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print("Withdrawal successful!")
        print("Remaining balance:", balance)


def atm():
    entered_pin = input("Enter your 4-digit PIN: ")

    if entered_pin != pin:
        print("Incorrect PIN! Access Denied.")
        return

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("Thank you for using our ATM!")
            break
        else:
            print("Invalid choice! Please try again.")


# Run the ATM program
atm()