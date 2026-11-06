class Car:
    def __init__(self,model,color,year,for_sale): #建立物件時自動執行
        self.model=model
        self.color=color
        self.year=year
        self.for_sale=for_sale

    def drive(self): #self代表呼叫這個方法的物件
        print(f"you drive the {self.color} {self.model}")
    def stop(self):
        print(f"you stop the {self.color} {self.model}")
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")