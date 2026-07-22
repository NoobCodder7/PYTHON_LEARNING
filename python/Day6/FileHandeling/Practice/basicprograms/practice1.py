# write a program to read a text from a given certificate.txt and find weather it contains word live 

file = open("certificate.txt")
data = file.read()

data = data.lower()

if "live" in  data:
    print("yes")
else:
    print("no")