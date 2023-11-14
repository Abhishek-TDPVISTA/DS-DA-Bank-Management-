import Auth  as auth

print("Welcome to the bank of Python")

print("Please Choice Option 1.Login 2.Register")

choice = int(input("Enter your choice: "))

if choice == 1:
    auth.Login()
elif choice == 2:
    if auth.Register() == True:
        auth.Login()    
    


