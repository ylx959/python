students={"sss","aaa","sandy"}

student=input("enter the name of a student: ")

if student in students: #in 檢查項目是否在集合裡
    print(f"There is {student}")
else:
    print(f"{student} is not found")