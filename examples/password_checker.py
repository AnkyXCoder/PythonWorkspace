# Password Checker Exercise

user_name = input("Enter your name: ")
password = input("Enter your password: ")
password_secret = input("Enter your password secret is:")
password_length = len(password)
hidden_password = '*' * password_length

print(f"Hey {user_name}, your password {hidden_password} is {password_length} letters long.")
