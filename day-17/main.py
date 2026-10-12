class User:
    pass

user_1 = User()

# this seems like a rather craptastic way to define class attributes
user_1.id = "001"
user_1.user_name = "angela"

print(user_1.user_name)