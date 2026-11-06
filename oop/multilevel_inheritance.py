class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print("This animal is fleeing")

class Predator(Animal):
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey): #多層繼承：Rabbit -> Prey -> Animal
    pass #沒有新內容，全部沿用父類別

class Fish(Prey, Predator): #多重繼承：同時有兩個父類別
    pass

class Hawk(Predator):
    pass

rabbit=Rabbit("Tony")
hawk=Hawk("Ray")
fish=Fish("Maggie")

rabbit.flee()

fish.flee()
fish.hunt()
hawk.hunt()

rabbit.eat()