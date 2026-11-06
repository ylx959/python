from script1 import * #import後可以直接用favorite_food

def favorite_drink(drink):
    print(f"Your favorite drink is {drink}")

def main():
    print("This is script2")
    favorite_food("sushi")
    favorite_drink("coffee")
    print("GoodBye")

if __name__=='__main__':
    main()

