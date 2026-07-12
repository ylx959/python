# Python reading files (.txt, .json, .csv)


file_path="input.txt"

try:
    with open(file_path,"r") as file:
        content=file.read()
        print(content)
except FileExistsError:
    print("that file was not found")
except PermissionError:
    print("you do not have permission to read that file")

    

