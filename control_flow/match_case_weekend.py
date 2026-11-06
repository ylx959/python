#match-case like switch

def day_of_week(day):
    match day:
        case "Sunday"|"Saturday":
            return True
        case "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday"|"Saturday"|"Sunday":
            return False
        case _:
            return False
        

user=input("enter the day: ")
print(day_of_week(user))


      