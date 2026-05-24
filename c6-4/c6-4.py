# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object
#oop
class car:
    def __init__(self,model,color,year,for_sale):
        self.model=model
        self.color=color
        self.year=year
        self.for_sale=for_sale

car1=car("bmw","red","2023","False")

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

