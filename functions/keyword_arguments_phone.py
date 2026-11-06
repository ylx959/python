#keyword argument

def get_phone(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"

phone_num=get_phone(country=12,area=23,first=233,last=2323) #寫出參數名稱比較好讀

print(phone_num)