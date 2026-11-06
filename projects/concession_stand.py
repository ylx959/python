#concession stand program

menu={  "pizza":3.00,
        "nachos":4.50,
        "popcorn":8.50,
        "hotdog":6.50,
        "coke":7.00,
        "chip":3.00,
        "fries":4.50,
        "soda":2.50,
}

cart=[]
total=0
print("-------MENU--------")
for key,value in menu.items():
    print(f"{key:10}:${value:.2f}") #:10 讓文字佔10格，菜單才會對齊
    
print("-------------------")

while True:
    food=input("Select an item(q to quit): ").lower()
    if food=="q":
        break
    elif menu.get(food) is not None: #get找不到時回傳None
        cart.append(food)
    else:
        print(f"{food} is not on the menu")

print("------YOUR ORDER------")
for food in cart:
    total=total+menu.get(food)
    print(food,end=" ")
print()


print(f"Total is: ${total:.2f}")