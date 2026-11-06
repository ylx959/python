import json
import csv



employee={
    "name":"Spongebob",
    "age":30,
    "job":"cook"
}

file_path="output.json"

try:
    with open(file_path,"a") as file:
        json.dump(employee,file,indent=4)
        print(f"txt_file {file_path} was created")
except FileExistsError:
    print("That file already exists !")

finally:
     print(f"Dict:employee have been added to File:{file_path}")