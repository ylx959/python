#list comprehension !!!! 

double=[x*2 for x in range(1,11)] #[運算式 for 變數 in 可迭代物件]
triple=[y*3 for y in range(1,11)]
square=[z*z for z in range(1,11)]
print(double)
print(triple)
print(square)

fruits=["apple","orange","banana","coconut"]
fruit_chart=[fruit[0] for fruit in fruits] #取每個水果的第一個字母
fruits=[fruit.upper() for fruit in fruits]

print(fruit_chart)
print(fruits)
