import random
lowest_num=1
highest_num=100
answer=random.randint(lowest_num,highest_num)
guesses=0
is_running=True
print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess=input("enter your guess:")

    if guess.isdigit(): #先確認是數字才能轉成int
        guess=int(guess)
        guesses+=1

        if guess <lowest_num or guess>highest_num:
            print("that number is out of range")
            print(f"Select a number between {lowest_num} and {highest_num}")
        elif guess <answer:
            print("too low try again")
        elif guess> answer:
            print("too high try again")
        else:
            print(f"Correct! The answer was {answer}")
            print(f"number of guesses: {guesses}")
            break
        
    else:
        print("Invalid guess")
        print(f"Select a number between {lowest_num} and {highest_num}")