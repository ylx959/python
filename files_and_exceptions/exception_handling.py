# exception = An event that interrupts the flow of a program
#                     (ZeroDivisionError, TypeError, ValueError)
#                     1.try, 2.except, 3.finally

#to prevent user input you dont have to use if else

try:
    number=int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError: #由上往下比對，具體的例外要寫在前面
    print("you can't divide by zero IDIOT")
except ValueError:
    print("Enter only numbers please !")
except Exception: #接住其他所有例外
    print("Something went wrong !")
finally: #不管有沒有錯誤都會執行
    print("Do some cleanup here")


