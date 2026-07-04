# zip() = Combines multiple iterables (lists, tuples, sets, dict)
#             into a single iterator of tuples.
#             Makes managing multiple indices easier.
#!!!!!!! important and convenience

names=["Spongebob","Patrick","Squiedward"]
ages=[20,50,49]
jobs=["cook","cashier","designer"]

datas=zip(names,ages,jobs)

#datas=dict(sorted(datas.items(),key=lambda data:data[1]))

for name,age,job in datas:
    print(f"{name} is {age} years old")



