import csv

file_path="input.csv"

try:
    with open(file_path,"r") as file:
        reader=csv.reader(file)
        for line in reader:
            print(line[0])
    
except FileExistsError:
    print("the file was not exist")