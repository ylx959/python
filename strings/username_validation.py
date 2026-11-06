#validate user input exercise

username=input("Enter your name: ")



if len(username)>12:
    print("your username can't be morethan 12 characters")
elif not username.find(" ")==-1: #find回傳-1代表找不到空白
    print("your username can't contain spaces")
elif not username.isalpha(): #isalpha只有全部是字母才會是True
    print("your username can't contain number")
else:
    print(f"Welcome {username}")