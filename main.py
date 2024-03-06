def login_user(user_name):
    
    usernames = ['John', 'Johnny', 'Jimmy', 'Joe', 'Spike']
    
    if user_name not in usernames:
        
        print("Invalid user name, please try again.")
    
    else:
        greeting = f"Welcome, {user_name}, we have been waiting for you."
        print(greeting)

# Look at my super awesome code! Yeah!
user_name = input("Please enter your name : ")
login_user(user_name)

