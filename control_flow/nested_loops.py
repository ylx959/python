
row=int(input("enter the number of rows:"))
col=int(input("enter the number of columns:"))
symbol=input("enter the symbol you like:")

for x in range(row): #外層迴圈控制列
    for y in range(col): #內層迴圈控制欄
        print(symbol,end="") #end=""讓print不換行
    print() #印完一列後換行