students={"sss","aaa","sandy"}

student=input("enter the name o a student: ")

if student in students:
    print(f"There is {student}")
else:
    print(f"{student} is not found")