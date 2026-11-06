#membership operators

word="apple"

letter=input("guess a letter in the secret word: ")

if letter not in word: #not in 檢查字串裡沒有這個字母
    print(f"{letter} was not found")
else:
    print(f"there is a {letter}")
