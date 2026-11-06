#composition

class Engine:
    def __init__(self,horse_power):
        self.horse_power=horse_power

class Wheel:
    def __init__(self,size):
        self.size=size

class Car:
    def __init__(self,make,model,horse_power,wheel_size):
        self.make=make
        self.model=model
        self.engine=Engine(horse_power) #Car自己建立Engine，Car消失它也跟著消失
        self.wheels=[Wheel(wheel_size) for wheel in range(4)] #建立4個輪子
    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horse_power}(hp) {self.wheels[0].size} inches"

car1=Car("Benz","Amg",700,20)
car2=Car("Ford","mustang",500,18)

print(car1.display_car())
print(car2.display_car())

