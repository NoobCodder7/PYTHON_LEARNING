#17. Create a login system using username and password.

# 17. Create a Login System using Username and Password

correct_username = "admin"
correct_password = "12345"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login Successful!")
else:
    print("Invalid Username or Password.")