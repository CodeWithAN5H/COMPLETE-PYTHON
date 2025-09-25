# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter your name: ")

if len(username) > 12:
    print("Your name is too long")
elif username.find(" ") != -1:
    print("Your name must not contain space")
elif not username.isalpha():
    print("Your name is not alphanumeric")
else:
    print("Welcome " + username + "!")

