class Animal:
    alive=True

class Dog(Animal):
    def speak(self):
        print("WOOF !")

class Cat(Animal):
    def speak(self):
        print("MEOW !")

class Car:
    def speak(self):
        print("Honk")

animals=[Dog(),Cat()]

for animal in animals:
    print(animal.alive)
