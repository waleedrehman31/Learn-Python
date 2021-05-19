file = open("./data.csv", "w") # IT open a file or create new one if file does not eixst
file = open("./data.csv", "r+") # read and write
file = open("./data.csv", "a") # append file
file.write("ID, name, email\n")
file.write("1, Waleed, waleed@waleed.com\n")
file.write("2, Waleed, waleed@waleed.com\n")
file.write("3, Waleed, waleed@waleed.com\n")
file = open("./data.csv", "r") # Read the file
print(file.read())
for line in file:
     print(line)
print(file.readlines())
file.close()

with open("./data.csv", "r") as file:
    print(file.read())