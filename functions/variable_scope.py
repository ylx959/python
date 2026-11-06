#variable scope
#scope resolution local 變數   L->E->G->B

from math import e
e=3 #全域變數會蓋掉import進來的e
def func1():
    print(e) #函式內沒有e，所以往外層找

#e=4
func1()

def func2():
    x=1 #func3的外層變數(Enclosed)

    def func3():
        print(x) #先找自己，再找外層
    func3()

func2()
