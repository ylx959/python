price1=3.14159
price2=98765.34434455
price3=12.34
# ^ center :.xf. + ,
print(f"price 1 is {price1:.2f}") #.2f 代表四捨五入到小數第2位
print(f"price 2 is {price2:.5f}")
print(f"price 3 is {price3:.1f}")

print(f"price 2 is {price2:+,.2f}") #+ 顯示正負號，逗號加上千分位
print(f"price 3 is {price3:^10}|") #^10 代表在10格寬度內置中
