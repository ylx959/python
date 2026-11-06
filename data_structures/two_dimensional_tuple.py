num_pad=((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))


for row in num_pad:
    for symbol in row:
        print(f"{symbol}",end="")
    print()