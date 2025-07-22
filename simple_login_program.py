# Simple user database
users = {
    "alice": "password",
    "bob": "some"
}

# Track the current logged-in user
current_user = {"username": None}

# Decorator to restrict access to logged-in users
def login_required(func):
    def wrapper(*args, **kwargs):
        if current_user["username"]:
            return func(*args, **kwargs)
        else:
            print("❌ Access Denied: Please log in first.")
    return wrapper

# Function to log in the user
def login_user():
    attempts = 3
    while attempts > 0:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in users and users[username] == password:
            current_user["username"] = username
            print(f"✅ You are logged in as {username}\n")
            break
        else:
            attempts -= 1
            print(f"❌ Invalid username or password. Attempts left: {attempts}")
            if attempts == 0:
                print("🚫 Login attempts exceeded.\n")

# Function to log out the current user
def log_out():
    if current_user["username"]:
        print(f"👋 Logged out from {current_user['username']}\n")
        current_user["username"] = None
    else:
        print("⚠ No user is currently logged in.\n")

# Function to view user profile (login required)
@login_required
def view_profile():
    print(f"👤 Viewing profile for {current_user['username']}\n")

# Main menu loop
def main():
    while True:
        print("==== MENU ====")
        print("1. Log in")
        print("2. Log out")
        print("3. View Profile")
        print("4. Exit Program")
        try:
            action = int(input("Choose an option (1–4): "))
        except ValueError:
            print("❌ Invalid input. Please enter a number.\n")
            continue

        if action == 1:
            login_user()
        elif action == 2:
            log_out()
        elif action == 3:
            view_profile()
        elif action == 4:
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again.\n")

# Start the program
main()
