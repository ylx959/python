#list comprehension !!!! 

double=[x*2 for x in range(1,11)]
triple=[y*3 for y in range(1,11)]
square=[z*z for z in range(1,11)]
print(double)
print(triple)
print(square)

fruits=["apple","orange","banana","coconut"]
fruit_chart=[fruit[0] for fruit in fruits]
fruits=[fruit.upper() for fruit in fruits]

print(fruit_chart)
print(fruits)
