#keyword argument

def hello(greeting,title,first,last):
    
    print(f"{greeting},{title} {first} {last}")


hello("hello",title="Mr.",last="linhsuan",first="yang") #關鍵字參數可以不照順序，但要放在位置參數後面