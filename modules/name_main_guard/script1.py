
def favorite_food(food):
    print(f"Your favorite food is {food}")


def main():
    print("This is script1")
    favorite_food("pizza")
    print("Goodbye !")

if __name__=='__main__': #直接執行才會成立，被import時不會執行
    main()