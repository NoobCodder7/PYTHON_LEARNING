#2. Create a menu-driven banking system using functions.

balance = 10000

def check_balance():
    print(f"Your current balance is ₹{balance}")

def deposit(amount):
    global balance
    balance += amount
    print(f"₹{amount} deposited successfully to your account")    
    print(f"your updated balance is {balance}")

def widrawal(amount):
    global balance
    if amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
        print(f"₹{amount} withdrawn successfully.")
        print(f"Remaining Balance: ₹{balance}")

def menue():
    while True:
        print("\n===== Banking System =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
def banking_menu():
    while True:
        print("\n===== Banking System =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            amount = float(input("Enter amount to deposit: ₹"))
            deposit(amount)

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: ₹"))
            widrawal(amount)

        elif choice == "4":
            print("Thank you for using our Banking System!")
            break

        else:
            print("Invalid choice! Please try again.")

# Start the program
banking_menu()