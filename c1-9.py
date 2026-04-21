#while loop

name=input("enter your name: ")

while name=="" or not name.isalpha():
    print("you did not enter your name")
    name=input("enter your name: ")
print(f"Welcome {name}")


