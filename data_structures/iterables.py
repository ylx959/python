#Iterables

my_dictionary={"A":1,"B":2,"C":3}

for key,value in my_dictionary.items(): #可迭代物件都能放進for迴圈
    print(f"{key}:{value}")

numbers=[1,2,3]
for number in reversed(numbers): #reversed()從後面開始取
    print(number)

for letter in "ylx": #字串也可以一個字一個字取出
    print(letter)
