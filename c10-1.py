# Python reading files (.txt, .json, .csv)


file_path="input.txt"


with open(file_path,"r") as file:
    content=file.read()
    print(content)
