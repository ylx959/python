class Fruit:
    def __init__(self,name,calories):
        self.name=name
        self.calories=calories
    
    def __repr__(self):
        return f"{self.name}:{self.calories}"

fruits=[Fruit("banana",105),
        Fruit("apple",105),
        Fruit("orange",105),
        Fruit("coconut",105),
        ] 

fruits=sorted(fruits,key=lambda fruit:fruit.name,reverse=True)
fruits=sorted(fruits,key=lambda fruit:fruit.calories)
fruits=sorted(fruits,key=lambda fruit:fruit.calories,reverse=True )

print(fruits)