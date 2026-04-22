
row=int(input("enter the number of rows:"))
col=int(input("enter the number of columns:"))
symbol=input("enter the symbol you like:")

for x in range(row):
    for y in range(col):
        print(symbol,end="")
    print()    