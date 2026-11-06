num_pad=((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))


for row in num_pad: #每次取出一列
    for symbol in row: #再取出該列的每個符號
        print(f"{symbol}",end="")
    print()