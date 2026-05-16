grades={"Sandy":"A","Jack":"B","Park":"C","Patric":"S"}

while True:
    student=input("enter the name of a student: ")
    if student in grades:
        print(f"{student}'s grade is {grades[student]}")  # or grades.get(student)!!!!!!!!!!!!!!!!!
        break
    else:
        print(f"{student} is not found")
        continue