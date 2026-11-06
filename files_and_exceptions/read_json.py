import json

file_path="input.json"

try:
    with open(file_path,"r") as file:
        content=json.load(file) #把json內容轉成字典
        print(content)
except FileNotFoundError:
    print("the file does not exist")
except PermissionError:
    print("you do not have permission")