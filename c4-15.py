grades=[50,55,67,98,100,34,46,97,85,47,74]

passing_grades=[grades.index(grade) for grade in grades if grade>=60]

print(passing_grades)

