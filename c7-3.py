#static method

class Employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position
    
    def get_info(self):
        return f"{self.name}={self.position}"
   

    def is_valid_position(position):

        
        print(Employee.is_valid_position("Cook"))