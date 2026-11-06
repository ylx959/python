employees=["Eugene","Squidward","Spongebob","Patrick"]

file_path="output.txt"

try:
    with open(file_path,"w") as file: #"w"會覆蓋原本的內容
        for employee in employees:
            file.write(employee+"\n") #write不會自動換行
        print(f"txt_file {file_path} was created")
except PermissionError:
    print("you do not have permission to write that file")
else:
    print(f"List:employees has been added to File:{file_path}")