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

class Rabbit(Prey):
    pass

class Fish(Prey, Predator):
    pass

class Hawk(Predator):
    pass

rabbit=Rabbit("Tony")
hawk=Hawk("Ray")
fish=Fish("Maggie")

rabbit.flee()

fish.hunt()

rabbit.eat()