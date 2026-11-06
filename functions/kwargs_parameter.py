#*args!!!!!!!!!!! is tuple
#**kwargs is dictonary

def print_address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_address(street="123.st",city="Taipei",state="USA",zip="407",apt="sssss")