grades=[50,55,67,98,100,34,46,97,85,47,74]

passing_grades=[grade for grade in grades if grade>=60]
passing_indexes=[index for index,grade in enumerate(grades) if grade>=60] #enumerate同時取出索引和值

print(passing_grades)
print(passing_indexes)

