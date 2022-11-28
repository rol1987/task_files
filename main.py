import os
current = os.getcwd()
folder_name = "2.4.files"
file_name = "recipes.txt"
full_path = os.path.join(current, folder_name, file_name)
with open(full_path, "r", encoding = "utf8") as file:
    cook_book = {}
    rez = file.readline()

    print(rez)

    # for line in file:
    #     print(line)