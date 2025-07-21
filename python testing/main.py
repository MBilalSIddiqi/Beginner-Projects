#def fahrenheit_to_celsius(fahrenheit):
#return (fahrenheit - 32) * 5 / 9
#def celsius_to_fahrenheit(celsius):
#return (celsius * 9 / 5) + 32
#choice = input('celsius or fahrenhiet ')
#if choice == 'celsius' or 'c':
#celsius = float(input("Enter temperature in Celsius: "))
#fahrenheit = celsius_to_fahrenheit(celsius)
#print(f"{celsius}°C is equal to {fahrenheit}°F")
#elif choice == 'fahrenhiet' or 'f':
#fahrenheit = float(input("Enter temperature in Fahrenheit: "))
#celsius = fahrenheit_to_celsius(fahrenheit)
#print(f"{fahrenheit}°F is equal to {celsius}°C")
#else:
#print("Invalid choice. ")


user1_tasks = [ '1.wake up' , '2.eat breakgfast' , '3.go to school' ]
user2_tasks = [ '1.wake up' , '2.eat break fast' ]

#class Login_program :
#def __init__(self , name , password) :
#self.name = name
#self.name = provided_name
#self.password = provided_password


#provided_name = input('Enter your user name: ')
#provided_password = input('Enter your password: ')

#if provided_name in user1[ 0 ] and provided_password in user1[ 1 ] :
#print('the user 1 is logged in')
#show_task: str = input("Do you want to see your tasks: ")
#x = show_task
#if show_task == 'n':
#print('ok')
#elif show_task in "y":
#print(*user1_tasks)
#add_tasks: str = input("do u wan to add tasks")
#if add_tasks in "y":
#what_tasks: str = input("write the task here :")
#z=user1_tasks.append(what_tasks)
#print(z)
#elif provided_name in user2[ 0 ] and provided_password in user2[ 1 ]:
#print('the user 2 is logged in')
#print(x)
#elif x in "y":
#print(*user2_tasks)
#elif x in 'n':
#print('ok')
#add_tasks: str = input("do u wan to add tasks")
#if add_tasks in "y":
#what_tasks1: str = input("write the task here :")
#y=user2_tasks.append(what_tasks1)
#print(y)


#add_tasks=input('Do you want to add taks Y/N ')


#mai ye kais karo ki agar user 1 yes bolai to user kai tasks ai aor
#user2 likaha to user 2 ke tasks ai


#else:
#print('user name or password is wrong')

#task1=input('do u want to know your tasks Y/N: ')
#if task1 == 'Y' or 'y' or 'yes':
#print(*user1_tasks)
#elif task1 == 'n':
#print('ok')

#or provided_name in user2[0] and provided_password in user2[1]or provided_name in user2[0] and provided_password in user2[1]


#def login_of_user1():
#print("user is logged in")
#def password_of_user1():
#print("password is correct")
#match input("enter your user name"):
#case "bilal":
#login_of_user1()
#match input("Enter your password"):
#case "1234":
#password_of_user1()
#case _:
#print("invalid user name or password")


#provided_name not in user1[0] and provided_password not in user1[1] or provided_name not in user2[0] and provided_password not in user2[1]:

# Dictionary containing usernames and passwords
user_name = {
    'user1': 'password123',
    'user2': 'mypassword',
    'user3': 'securepass'
}

def check_credentials(username, password):
    """Check if the provided username and password match the records."""
    if username in user_name:
        if user_name[username] == password:
            return "Login successful!"
        else:
            return "Incorrect password."
    else:
        return "Username does not exist."

def sign_up(username, password):
    """Add a new user to the user_name dictionary."""
    if username in user_name:
        return "Username already exists. Please choose another one."
    else:
        user_name[username] = password
        return "Sign-up successful!"

# Example usage        
while True:
    action = input("Would you like to (1) Log in or (2) Sign up? Enter 1 or 2: ")

    if action == '1':
        username_input = input("Enter your username: ")
        password_input = input("Enter your password: ")
        result = check_credentials(username_input, password_input)
        print(result)
    elif action == '2':
        new_username = input("Enter a new username: ")
        new_password = input("Enter a new password: ")
        result = sign_up(new_username, new_password)
        print(result)
    else:
        print("Invalid option. Please choose 1 or 2.")

    continue_prompt = input("Would you like to continue? (yes/no): ")
    if continue_prompt.lower() != 'yes':
        break































user1={'name':'bilal','password':'1234'}
user2={'name':'hasan','password':'12345'}
checking_users=(user1.keys())

def line():
    print('-----------------------------')
def login():
    print("     Login Program       ")
    check_user=input("Enter your user name: ")
    check_password=input('Enter your password: ')
    if check_user == user1['name'] :
        print('the username is correct')
        if check_password == user1['password']:
            print('The password is correct')
        print(' you are now logged in user 1')
        print('-----------------------------')
    elif check_user == user2['name'] :
        print('the username is correct')
        if check_password == user2['password']:
            print('The password is correct')
            print(' you are now logged in user 2')
            print ( '-----------------------------')
    elif check_user =='' or check_password =='':
        print('Error')
        line()
    else:
        print("USER NAME OR PASSWORD IS INVALID")
        line()
def sign_up():
    pass
    line()


is_running=True
while is_running==True:
    print("Welcome to the login program")
    line()

    print('1.Login')
    print('2.Sign up')
    print('3.Exit')
    choice = input ( 'Please choose an option: ' )
    line()

    if choice == '1':
        login()
    elif choice == '2':
        sign_up()
    elif choice == '3':
        print ( 'Have a nice day' )
        line()
        break

    else:
        print("that's not a valid choice")