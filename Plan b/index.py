# User database (replace this with a secure storage method)
user_database = {"user1": "password1", "user2": "password2"}

def login(username, password):
    if username in user_database and user_database[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password")

def register(username, password):
    if username not in user_database:
        user_database[username] = password
        print("Registration successful!")
    else:
        print("Username already exists. Please choose a different username.")

while True:
    print("1. Login")
    print("2. Register")

    user_pick = int(input("Choose number: "))

    if user_pick == 1:
        print("Login")
        input_username = input("Username: ")
        input_password = input("Password: ")
        login(input_username, input_password)

    elif user_pick == 2:
        print("Register")
        input_username = input("Username: ")
        input_password = input("Password: ")
        register(input_username, input_password)

    else:
        print("Invalid choice. Please choose 1 or 2.")
