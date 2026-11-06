#nested class
class Company:

    class Employee: #Employee只在Company內使用，所以寫在裡面
        def __init__(self, name, position):
            self.name = name
            self.position = position
        def get_details(self):
            return f"{self.name}:{self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name,position):
        new_employee=self.Employee(name,position) #用self取得內部類別
        self.employees.append(new_employee)

    def list_employee(self):
        return [person.get_details()
                for person in self.employees]


company1= Company("Apple")
company2=Company("Google")


company1.add_employee("Jack","Designer")
company1.add_employee("Jennie","Engineer")
company1.add_employee("Terry","PM")

company2.add_employee("Jack","Designer")
company2.add_employee("Jennie","Engineer")
company2.add_employee("Jerry","XR Engineer")

for employee in company1.list_employee():
    print(employee)

for employee in company2.list_employee():
    print(employee)