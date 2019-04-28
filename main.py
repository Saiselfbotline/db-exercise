from users import User

# Init user
user = User()

# var mid for test, this is userId in LINE Protocol
mid = "uc86fb39275d33ba1b513cf7291c73e81"

# function to add user
user.add(mid)

# function to delete user
user.delete(mid)

# function to show list user
user.list()

# check if mid in users
if mid in user.list():
    print(f"{mid} is users")
