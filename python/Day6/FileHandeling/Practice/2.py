try: 
    with open("newfile.txt" , "x")as file:
        file.write("This is a new file")
    print("File created successfully")

except FileExistsError:
        print("File already exists.")
    