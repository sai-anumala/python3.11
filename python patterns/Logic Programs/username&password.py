username=input("Enter your username:")
password=input("Enter your paswword:")
password_length=len(password)
hidden_password="*"*password_length
print(f"{username} and password is {hidden_password} and its length is {password_length}")