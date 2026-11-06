#hangman in python
import random
from wordlist import words

#dictionary of key:()
hangman_art = {

    0: (
        "   ",

        "   ",

        "   "
    ),

    1: (
        " o ",

        "   ",

        "   "
    ),

    2: (
        " o ",

        " | ",

        "   "
    ),

    3: (
        " o ",

        "/| ",

        "   "
    ),

    4: (
        " o ",

        "/|\\",

        "   "
    ),

    5: (
        " o ",

        "/|\\",

        "/  "
    ),

    6: (

        " o ",

        "/|\\",

        "/ \\"
    )

}

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))
def display_answer(answer):
    print(" ".join(answer))

def main():
    answer=random.choice(words)
    hint=["_"]*len(answer) #用底線代表還沒猜到的字母
    wrong_guesses=0
    guessed_letters=set() #important
    is_running=True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess=input("Enter a letter: ").lower()
        
        if len(guess)!=1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue
            
        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] ==guess: #同一個字母可能出現很多次，所以全部檢查
                    hint[i]=guess
        else:
            wrong_guesses+=1

        if "_" not in hint:
            display_answer(answer)
            print("you win")  
            break

        if wrong_guesses>=len(hangman_art)-1: #畫完最後一張圖就結束
            print(f"Game over the answer is : {answer}")
            is_running=False

    
    
            

if __name__=='__main__':
    main()