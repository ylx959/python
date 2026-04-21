#validate user input exercise

username=input("Enter your name: ")



if len(username)>12:
    print("your username can't be morethan 12 characters")
elif not username.find(" ")==-1:
    print("your username can't contain spaces")
elif  not username.isalpha():
     print("your username can't contain number")
else:
    print(f"Welcome {username}")