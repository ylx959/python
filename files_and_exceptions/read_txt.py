# Python reading files (.txt, .json, .csv)


file_path="input.txt"

try:
    with open(file_path,"r") as file: #with結束後會自動關閉檔案
        content=file.read()
        print(content)
except FileNotFoundError: #讀檔時檔案不存在會觸發這個例外
    print("that file was not found")
except PermissionError:
    print("you do not have permission to read that file")

    

