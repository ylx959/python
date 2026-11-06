
def read_file(file_path):
    with open(file_path) as file:
        for line in file:
            yield line.strip() #一次只讀一行，大檔案也不會佔滿記憶體

file_path="lord_of_the_rings.txt"


for line in read_file(file_path):
    print(line)
