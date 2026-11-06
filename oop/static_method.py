#static method

class Employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position

    def get_info(self):
        return f"{self.name}={self.position}"

    @staticmethod #不需要self，和物件資料無關的工具函式
    def is_valid_position(position):
        valid_positions=["Manager","Cashier","Cook","Janitor"]
        return position in valid_positions

employee1=Employee("Eugene","Manager")
employee2=Employee("Squidward","Cashier")

print(employee1.get_info())
print(employee2.get_info())

print(Employee.is_valid_position("Cook")) #直接用類別名稱呼叫
print(Employee.is_valid_position("Rocket Scientist"))
