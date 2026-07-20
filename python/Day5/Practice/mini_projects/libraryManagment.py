# Mini Library Management System Using Functions

library = ["Python", "Java", "C++", "SQL", "Data Science"]
issued_books = []


def display_books():
    print("\nAvailable Books:")
    if len(library) == 0:
        print("No books available.")
    else:
        for book in library:
            print("-", book)


def issue_book():
    book = input("Enter the book name to issue: ")

    if book in library:
        library.remove(book)
        issued_books.append(book)
        print(book, "has been issued successfully.")
    else:
        print("Book is not available.")


def return_book():
    book = input("Enter the book name to return: ")

    if book in issued_books:
        issued_books.remove(book)
        library.append(book)
        print(book, "has been returned successfully.")
    else:
        print("This book was not issued from this library.")


def add_book():
    book = input("Enter the new book name: ")
    library.append(book)
    print(book, "has been added to the library.")


def library_menu():
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Display Available Books")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Add Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_books()
        elif choice == "2":
            issue_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            add_book()
        elif choice == "5":
            print("Thank you for using the Library Management System!")
            break
        else:
            print("Invalid choice! Please try again.")


# Run the program
library_menu()