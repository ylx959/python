#python writing files(.txt .json .csv)

txt_data="I love to drink coffee"

file_path="output.txt"
try:
    with open(file_path,"a") as file: #"a"附加在檔案尾端，檔案不存在會自動建立
        file.write("\n"+txt_data)
except PermissionError:
    print("you do not have permission to write that file")
else:
    print(f"Text:{txt_data} has been added to File:{file_path}")

