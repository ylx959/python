#*args!!!!!!!!!!! is tuple
#**kwargs is dictionary

def print_address(**kwargs): #傳進來的關鍵字參數全部收進字典
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_address(street="123.st",city="Taipei",state="USA",zip="407",apt="sssss")