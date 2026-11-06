#while loop

name=input("enter your name: ")

while name=="" or not name.isalpha(): #條件成立就一直重複，直到輸入正確
    print("you did not enter your name")
    name=input("enter your name: ")
print(f"Welcome {name}")


