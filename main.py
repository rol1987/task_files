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