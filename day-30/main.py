# FileNotFound
# with open("a_file.text") as file:
#     file.read

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["non_existent_key"])
# except FileNotFoundError:
#     file = open("a_file.txt","w")
# except KeyError as error_message: #capture the error message
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("file was closed")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 metres")
bmi = weight / height ** 2
print(bmi)

# Key error
# a_dictionary = {"key", "value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)