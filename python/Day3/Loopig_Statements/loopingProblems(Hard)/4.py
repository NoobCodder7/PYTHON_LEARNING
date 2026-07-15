# 6. Keep asking the user for a password until the correct password is entered.
correct_user_name = "admin"
correct_password = "admin123"

username = ""
password = ""

while username != correct_user_name or password != correct_password:
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username != correct_user_name or password != correct_password:
        print("Invalid username or password! Try again.\n")

print("Login Successful! Welcome.")