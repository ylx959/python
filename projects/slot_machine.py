#python slot machine
import random

def spin_row():
    symbols=['🍒','🍉','🍋','🔔','⭐️']
    return [random.choice(symbols) for symbol in range(3)] #隨機取3個符號

def print_row(row):
    print("***********")
    print("|".join(row))
    print("***********")

def get_payout(row,bet):
    if row[0]==row[1]==row[2]: #三個符號相同才有獎金
        if row[0]=='🍒':
            return bet*3
        elif row[0]=='🍉':
            return bet*4
        elif row[0]=='🍋':
            return bet*5
        elif row[0]=='🔔':
            return bet*10
        elif row[0]=='⭐️':
            return bet*20
    return 0

def main():
    balance=100
    print("***********************")
    print("welcome to python slots")
    print("Symbols:🍒 🍉 🍋 🔔 ⭐️")
    print("***********************")

    while balance > 0:
        print(f"current balance:${balance}")

        bet=input("place your bet amount: ")

        if not bet.isdigit():
            print("Please enter valid number")
            continue #輸入錯誤時回到迴圈開頭，不扣錢

        bet=int(bet)

        if bet>balance:
            print("Insufficient funds")
            continue
        
        if bet<=0:
            print("Bet must be greater than 0")
            continue
        
        balance-=bet

        row=spin_row()
        print("Spinning...\n")
        print_row(row)

        payout=get_payout(row,bet)

        if payout>0:
            print(f"you won ${payout}")
        else:
            print("Sorry you lost this round")
        
        balance+=payout
        play_again=input("Do you want to spin again? (Y/N): ").upper()
        if play_again !='Y':
            break
    
    print(f"Game over! Your final balance is ${balance}")


if __name__=='__main__':
    main()