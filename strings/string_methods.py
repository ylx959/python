name=input("enter your name: ")
phone_number=input("enter your phone number: ")

print(len(name)) #字串長度
print(name.find("y")) #回傳第一個y的位置，找不到回傳-1
print(name.capitalize()) #字串不可變，這些方法都是回傳新字串
print(name.upper())
print(name.isdigit()) #是否全部都是數字
print(name.isalpha()) #是否全部都是英文字母

print(phone_number.count("-")) #計算-出現幾次
phone_number=phone_number.replace("-","") #要重新指定變數才會保留結果
print(phone_number)
