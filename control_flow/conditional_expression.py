#temp=float(input("enter the temperature"))

#is_sunny=True

#if temp>=28 and is_sunny:
    #print("it is Hot outside")
#x if condition else y

temperature=20
user_role="admin"

weather="hot" if temperature>=25 else "cold" #一行寫完的if else

print(weather)

access_level="Full Access" if user_role=="admin" else "Limited Access"

print(access_level)



