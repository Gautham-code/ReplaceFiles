data = ""

with open("sample1.txt", "rb") as file:
    data = file.read()

with open("sample2.txt") as file1:
    with open("sample1.txt") as file2:
        file2.write(file1.read())

with open("sample2.txt") as file:
    file.write(data)
print("File Replaced")

del data