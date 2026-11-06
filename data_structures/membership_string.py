#membeeship operators

word="apple"

letter=input("guess a letter in the secret word: ")

if letter not in word:
    print(f"{letter} was not found")
else:
    print(f"there is a {letter}")
