number=int(input("Enter a number to square up to:"))

even_squares=(x**2 for x in range(1,number+1) if x%2==0) #用到時才計算，不會一次全部存起來

for square in even_squares:
    print(square)