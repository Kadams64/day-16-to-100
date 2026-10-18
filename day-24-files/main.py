# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with keyword adds automatic control of file closure
# when block exits
MYFILE = "../../../Desktop/my_file.txt"

with open(MYFILE) as file:
    contents = file.read()
    print(contents)

# basic file modes: r for read, w for write, a for append
with open(MYFILE, "a") as file:
    file.write("new text.\n")