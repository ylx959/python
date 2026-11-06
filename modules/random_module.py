import random

#print(help(random))

low=1
high=100
options=("rock","paper","scissors")
cards=["2","3","4","5","6","7","8","9","10","J","Q","K"]

print(random.choice(options)) #隨機選一個

random.shuffle(cards) #直接打亂原本的list
print(cards)

number=random.randint(low,high) #包含low和high
print(number)

number=random.random() #0到1之間的小數
print(number)
