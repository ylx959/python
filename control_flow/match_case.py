#match-case like switch

def day_of_week(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _: #_ 代表其他所有情況，像是switch的default
            return "Not a valid day"

enter=int(input("Enter the number: "))
print(day_of_week(enter))


      