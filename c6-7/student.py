class Student:
    
    class_year=2024
    num_students=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Student.num_students+=1

student1=Student("Jack",35)
student2=Student("Maggie",45)
student3=Student("Ray",34)
student4=Student("May",32)


print(f"My gradute class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)

