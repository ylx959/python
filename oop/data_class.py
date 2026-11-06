# Data Class = A special kind of class that's designed mostly for holding data
#                        without writing a lot of the boilerplate code for regular classes.
#                        They automatically generate: __init__, __repr__, __eq__
#                       (Python 3.7+)

from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    age: int
    password: str = field(repr=False) #repr=False讓print時不顯示密碼
    is_alive: bool = True

person1=Person("Spongebob",35,"3423424")
person2=Person("Patrick",30,"343424",False)

print(person1)
print(person2)
print(person1==person2) #自動產生的__eq__會比較所有欄位



