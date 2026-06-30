employees=["Eugene","Squidward","Spongebob","Patrick"]

file_path="output.txt"

try:
    with open(file_path,"w") as file:
        for employee in employees:
            file.write(employee+"\n")
        print(f"txt_file {file_path} was created")
except FileExistsError:
    print("That file already exists !")

finally:
     print(f"List:employees have been added to File:{file_path}")