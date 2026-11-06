#list comprehension !!!! 
numbers=[1,-2,3,-4,5,-6,8,10,22,-34,-31]

positive_nums=[num for num in numbers if num>0]
negative_nums=[num for num in numbers if num<0]
even_nums=[num for num in numbers if num%2==0]
print(positive_nums)
print(negative_nums)
print(even_nums)