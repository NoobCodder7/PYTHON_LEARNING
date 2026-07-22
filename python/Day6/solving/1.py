#1. Create a file named student.txt and write your name into it.
with open("Student.txt", "w") as file:
    file.write("Hello my name is viraj")

#2. Read and display the contents of a text file.
with open("Student.txt", "r") as file:
    print(file.read())


#3. Append a new line to an existing file.
with open("Student.txt", "a") as file:
    file.write("\nI am learning File Handeling")
print("Data has been appended successfully")
with open("Student.txt", "r") as file:
    print(file.read())

#4. Read only the first line of a file.

with open("Student.txt", "r") as file:
    print(file.readline())

#5. Read all lines using readlines().
with open("student.txt", "r") as file:
    lines = file.readlines()

print(lines)


# 6. Print each line of a file using a loop.

with open("student.txt", "r") as file:
    for line in file:
        print(line)

# 7. Count the number of lines in a file.
with open("Student.txt", "r") as file:
    line = file.readlines()
    print("Total lines = ", len(line))

# 8. Count the number of words in a file.
with open("Student.txt", "r") as file:
    data = file.read()

words = data.split()

print("Total words = ", len(words))


# 9. Count the number of characters in a file.
with open("student.txt", "r") as file:
    data = file.read()

print("Total Characters:", len(data))


#10. Check whether a file exists before opening it.

import os

if os.path.exists("student.txt"):
    with open("student.txt", "r") as file:
        print(file.read())
else:
    print("File does not exist.")


with open("student.txt", "w") as file:
    file.write("Python File Handling\n")
    file.write("Learning Write Mode")

print("File overwritten successfully.")



with open("Student.txt", "a") as file:
    file.write("\nPython")
    file.write("\nJava")
    file.write("\nC++")

print("Lines appended successfully.")


with open("Student.txt" , "r") as file:
    data = file.read()

print(data)



#16. Move the File Pointer Using seek()

with open("Student.txt", "r") as file:
    print("Current position ", file.tell())

    file.read(10)

    print("New Position:", file.tell())

# 17. Copy the Contents of One File into Another

with open("Student.txt", "r") as Source:
    data = Source.read()
with open("NewStudent.txt", "w") as Destination:
    Destination.write(data)
  
print("File copied successfully.")

#18. Merge Two Text Files into One

with open("Student.txt", "r") as f1:
    data1 = f1.read()

with open("NewStudent.txt" ,"r") as f2:
    data2 = f2.read()

with open("merge.txt", "w") as f3:
    f3.write(data1)
    f3.write("\n")
    f3.write(data2)

print("The data is merged into f3")





