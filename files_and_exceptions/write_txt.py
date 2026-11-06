#python writinh files(.txt .json .csv)

txt_data="I love to drink coffee"

file_path="output.txt"
try:
    with open(file_path,"a") as file:
        file.write("\n"+txt_data)
        print(f"The file:{file_path} was created")
except FileExistsError:
    print("That file already exist")
finally:
    print(f"Text:{txt_data} have been added to File:{file_path}")

