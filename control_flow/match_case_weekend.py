#match-case like switch

def is_weekend(day):
    match day:
        case "Sunday"|"Saturday": #| 代表符合其中一個就成立
            return True
        case "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday":
            return False
        case _:
            return False
        

user=input("enter the day: ")
print(is_weekend(user))


      