import json

file_path="input.json"

try:
    with open(file_path,"r") as file:
        content=json.load(file)
        print(content)
except FileExistsError:
    print("the file was not exist")
except PermissionError:
    print("you do not have permission")