# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

#          Relative Path
with open("../../../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)
#        Absolute Path
#        ("C:/Users/janob/Desktop/my_file.txt")

# with open("new_file.txt", mode="w") as file:
#     file.write("\nNew text. ")