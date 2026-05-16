#*args!!!!!!!!!!! is tuple
#**kwargs
def add(*args):
    total=0
    for arg in args:
        total+=arg
    return total


print(add(1,2,3,100,345))

