
import csv

employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]



file_path="output.csv"

try:
    with open(file_path,"w",newline="") as file: #newline=""避免多出空白行
        writer=csv.writer(file)
        for row in employees:
            writer.writerow(row) #一次寫入一列
        print(f"csv_file {file_path} was created")
except PermissionError:
    print("you do not have permission to write that file")

