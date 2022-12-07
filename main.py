# Задача №1

import os
current = os.getcwd()
folder_name = "2.4.files"
file_name = "recipes.txt"
full_path = os.path.join(current, folder_name, file_name)

with open(full_path, "r", encoding = "utf8") as file:
    dish = []
    # НЕМНОГО ПОЧИСТИМ СПИСОК ОТ ПУСТЫХ СТРОК И ЧИСЛОВЫХ СТРОК
    for line in file:
        if line.strip() == "": 
            continue
        else:
            dish.append(line.strip())
    # ПЕРЕБОР ОЧИЩЕННОГО СПИСКА
    master_dict = {}
    cook_dict = {}
    cooc_list = []
    for count in dish:
        num_element = dish.index(count)  
        if dish[num_element].isdigit():
            len_count = int(count)
            cooc_list = []
        elif dish[num_element].find("|") == -1:
            dish_name = count
            master_dict[dish_name] = cooc_list       
        elif dish[num_element].find("|") != -1:
            rez = dish[num_element].split(' | ')
            cook_dict["ingredient_name"] = rez[0]
            cook_dict["quantity"] = rez[1]
            cook_dict["measure"] = rez[2]
            cooc_list.append(cook_dict)
            cook_dict = {}
        master_dict[dish_name] = cooc_list         
print(master_dict)
print()
file.close()

# ЗАДАЧА №2
def get_shop_list_by_dishes(dishes, person_count):
    shop_list_by_dishes = {}
    for dish in dishes:
        for key, value in master_dict.items():
            if dish == key:
                for val in value:
                    shop_list = {"measure": "", "quantity": 0}
                    ingredient_name = val["ingredient_name"]
                    shop_list["measure"] = val["measure"]
                    shop_list["quantity"] = int(val["quantity"]) * person_count
                    shop_list_by_dishes[ingredient_name] = shop_list
    print(shop_list_by_dishes)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 3)


# ЗАДАЧА №3
current = os.getcwd()
folder_name = "2.4.files\sorted" 
file_list = []

for root, dirs, files in os.walk(os.path.join(current, folder_name)):  
    for filename in files:
        file_list.append(filename)

dict_line_in_files = {}

for file_name in file_list:
    full_path = os.path.join(current, folder_name, file_name)
    with open(full_path, "r", encoding = "utf8") as file:
        dict_line_in_files[file_name] = len(file.readlines())
        sorted_tuple = sorted(dict_line_in_files.items(), key=lambda x: x[1])
        dict_line_in_files = dict(sorted_tuple)
    file.close()

result_file_name = "result.txt"
result_full_path = os.path.join(current, result_file_name)
with open(result_full_path, "a", encoding = "utf8") as result_file:
    for file_key, count_line in dict_line_in_files.items():   
        full_path = os.path.join(current, folder_name, file_key)
        with open(full_path, "r", encoding = "utf8") as sorted_file:
            result_file.write(f"{file_key}\n")
            result_file.write(f"{count_line}\n")
            for line in sorted_file:
                result_file.write(f"{line}\n")
result_file.close()


