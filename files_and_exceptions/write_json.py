import json



employee={
    "name":"Spongebob",
    "age":30,
    "job":"cook"
}

file_path="output.json"

try:
    with open(file_path,"w") as file: #json要用"w"，用"a"附加會讓格式壞掉
        json.dump(employee,file,indent=4) #indent讓輸出有縮排比較好讀
        print(f"json_file {file_path} was created")
except PermissionError:
    print("you do not have permission to write that file")
else: #沒有發生錯誤才會執行
    print(f"Dict:employee has been added to File:{file_path}")