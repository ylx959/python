def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg)
    print()
    
    print(f"{kwargs.get('street')}")


shipping_label("Dr.","spongebob","Squarepants","III",
                street="123.st",
                apt="100",
                city="Detroit",
                state="Mi",
                zip="54321")

