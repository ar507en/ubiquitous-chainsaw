users = []


class User:

    user_count = 0

    def __init__(self, name, age, password):
        self.name = name
        self.age = age
        self.password = password
        self.reg_number = self.user_count
        self.user_count += 1

    def get_user_count(self):
        return self.user_count+1


def throw_error():
    print("Error. Invalid input. Please try again.")


def reg_or_log_page():
    command = input("Would you like to register or log in? (r/l)\t")
    match command:
        case "r":
            reg_page()
            # go to reg page
        case "l":
            log_page()
            # go to log page
        case _:
            throw_error()
            reg_or_log_page()
            # try again


def reg_page():
    pw_length = 4
    age_restriction = 18
    age = int(input("Please enter your age\t"))
    if age < age_restriction:
        throw_error()
        reg_page()
    username = input("Please enter the username of your choosing\t")
    # check if already taken
    password = input(f"Please enter a valid password (length has to be at least {pw_length} characters long\t")
    if len(password) < pw_length:
        throw_error()
        reg_page()
    users.append(User(username, age, password))


def log_page():
    pass


# main program
reg_or_log_page()


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
