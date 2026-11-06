#*args!!!!!!!!!!! is tuple
#**kwargs
def add(*args): #傳幾個參數都可以，全部收進tuple
    total=0
    for arg in args:
        total+=arg
    return total


print(add(1,2,3,100,345))

