# with open("sample.txt", "w") as file:
#     #     content = file.read()
#     # print(content)

#     file.write("Hello World")
#     file.writelines(["Alice", "Bob", "Cat"])


# statement 'with' makes sure that opened file was automatically saved


try:
    with open("sample.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
