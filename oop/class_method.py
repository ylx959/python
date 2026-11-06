#class method

class Student:
    count=0
    total_gpa=0
    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        Student.count+=1 #類別變數由所有物件共用
        Student.total_gpa+=gpa


    def get_info(self):
        return f"{self.name} :{self.gpa}"

    @classmethod #cls代表類別本身，用來操作類別變數
    def get_count(cls):
        return f"Total # of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count==0:
            return 0
        else:
            return f"Average gpa:{(cls.total_gpa/cls.count):.2f}"

student1=Student("Jack",3.65) 
student2=Student("Jay",3.45)
student3=Student("Jace",4.23)

print(student1.get_info())
print(Student.get_count())
print(Student.get_average_gpa())
