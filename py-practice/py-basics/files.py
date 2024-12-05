# file i/o
# fr= open("file.txt")
# data = fr.read()
# print(data)

# name = "bidur"
# fl = open("file2.txt", "w")
# fl.write(f"my name is: {name}")
# fl.close()
# print("File is created in given path check it out")

fil = open("file.txt", "r")
reading = fil.readlines()
print(reading)
fil.close()