def shipping_label(*args,**kwargs): #*args要寫在**kwargs前面
    for arg in args:
        print(arg,end=" ")
    print()

    print(f"{kwargs.get('street')} {kwargs.get('apt')}") #get找不到key時回傳None，不會報錯
    print(f"{kwargs.get('city')},{kwargs.get('state')} {kwargs.get('zip')}")


shipping_label("Dr.","spongebob","Squarepants","III",
                street="123.st",
                apt="100",
                city="Detroit",
                state="Mi",
                zip="54321")

