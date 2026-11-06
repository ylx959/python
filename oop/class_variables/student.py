class Student:
    
    class_year=2024 #寫在__init__外面的是類別變數
    num_students=0
    def __init__(self,name,age):
        self.name=name #self開頭的是每個物件自己的變數
        self.age=age
        Student.num_students+=1 #每建立一個物件就加1

student1=Student("Jack",35)
student2=Student("Maggie",45)
student3=Student("Ray",34)
student4=Student("May",32)


print(f"My graduate class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)

