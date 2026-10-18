# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with keyword adds automatic control of file closure
# when block exits
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# basic file modes: r for read, w for write, a for append
with open("my_file.txt", "a") as file:
    file.write("new text.\n")