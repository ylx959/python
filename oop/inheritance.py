#inheritance

class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True

    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal): #Dog繼承Animal的屬性和方法
    def speak(self):
        print("woof")
    
class Cat(Animal):
    def speak(self):
        print("meow")

class Mouse(Animal):
    def speak(self):
        print("squeek")

dog=Dog("Dexter")
cat=Cat("Maggie")
mouse=Mouse("Lili")

dog.speak()
cat.speak()
mouse.speak()

dog.eat() #eat定義在父類別，子類別可以直接用
cat.sleep()
print(mouse.is_alive)

