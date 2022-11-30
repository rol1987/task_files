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
    num_element = 0
    len_count = 0
    len_dish = len(dish)
    cook_book = {}
    cooc_list = []
    x = 0
    for count in dish:
        num_element = dish.index(count)  
        x += 1
        if dish[num_element].isdigit():
            len_count = int(count)
            cooc_list = []
        elif dish[num_element].find("|") == -1:
            dish_name = count
            master_dict[dish_name] = cooc_list       
        elif dish[num_element].find("|") != -1:
            rez = dish[num_element].split(' | ')
            cook_book["ingredient_name"] = rez[0]
            cook_book["quantity"] = rez[1]
            cook_book["measure"] = rez[2]
            cooc_list.append(cook_book)
            cook_book = {}
        master_dict[dish_name] = cooc_list         
print(master_dict)    