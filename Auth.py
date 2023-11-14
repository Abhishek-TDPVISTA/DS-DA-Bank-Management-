
def Login():
    print("Login")
    print("Enter your username")
    username = input("Enter your username: ")
    print("Enter your password")
    password = input("Enter your password: ")
    print("Welcome " + username + " to the bank of Python")
    print("Your password is " + password)
    print("Thank you for banking with us")
    return True

def Register():
    print("Register")
    print("Enter your username")
    username = input("Enter your username: ")
    print("Enter your password")
    password = input("Enter your password: ")
    print("Enter your password again")
    password2 = input("Enter your password again: ")
    if password != password2:
        print("Password does not match")
        Register();    
    print("Welcome " + username + " to the bank of Python")
    print("Your password is " + password)
    print("Thank you for banking with us")
    return True

