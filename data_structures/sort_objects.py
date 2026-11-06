class Fruit:
    def __init__(self,name,calories):
        self.name=name
        self.calories=calories

    def __repr__(self): #print物件時顯示的文字
        return f"{self.name}:{self.calories}"

fruits=[Fruit("banana",105),
        Fruit("apple",72),
        Fruit("orange",73),
        Fruit("coconut",354),
        ]

print(sorted(fruits,key=lambda fruit:fruit.name,reverse=True)) #key決定用哪個屬性排序
print(sorted(fruits,key=lambda fruit:fruit.calories))
print(sorted(fruits,key=lambda fruit:fruit.calories,reverse=True))
