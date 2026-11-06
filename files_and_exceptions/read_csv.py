import csv

file_path="input.csv"

try:
    with open(file_path,"r",newline="") as file:
        reader=csv.reader(file) #每一行會變成一個list
        for line in reader:
            print(line)
    
except FileNotFoundError:
    print("the file does not exist")
except PermissionError:
    print("you do not have permission")