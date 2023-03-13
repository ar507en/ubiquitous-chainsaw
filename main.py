

class User:

    def __int__(self, name, age, password):
        self.name = name
        self.age = age
        self.password = password


current_input = input("Would you like to register or log in? (r/l)\t")


# PSEUDOCODE:
# Ask User for Login or Registration
# 1. Registration:
# Ask User for Username, age & Password
# Check if username is already taken and if age and password are valid
# if valid, create permanent account

# 2. Login:
# Ask user for username & password
# check if username exists
# check if username and password align
# if valid, let the user be logged in
