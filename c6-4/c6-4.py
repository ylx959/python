# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object
#oop
from car import Car

car1=Car("bmw","red","2023","False")
car2=Car("benz","white","2004","True")
car3=Car("toyota","blue","2012","False")


print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

car3.drive()
car2.stop()
car1.describe()

