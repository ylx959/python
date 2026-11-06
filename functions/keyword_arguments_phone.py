#key word arguement

def get_phone(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"

phone_num=get_phone(country=12,area=23,first=233,last=2323)

print(phone_num)