class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0 # default value

user_1 = User("001", "angela")

# this seems is a bit cleaner

print(user_1.user_name)