def dict_recipes(file_recipes):
    with open(file_recipes, 'r') as file_work:
        menu_dict = {}
        for line in file_work:
            dish_name = line[:-1]
            counter = file_work.readline().strip()
            list_ingredient = []
            for i in range(int(counter)):
                dish_items = dict.fromkeys(['ingredient_name', 'quantity', 'measure'])
                ingridient = file_work.readline().strip().split(' | ')
                for item in ingridient:
                    dish_items['ingredient_name'] = ingridient[0]
                    dish_items['quantity'] = ingridient[1]
                    dish_items['measure'] = ingridient[2]
                list_ingredient.append(dish_items)
                cook_book = {dish_name:list_ingredient}
                menu_dict.update(cook_book)
            file_work.readline()
    return(menu_dict)


def get_dishes(dishes, persons=int):
    menu_dict = dict_recipes('reciepts_initial.txt')
    shop_list = {}
    for dish in dishes:
        for item in (menu_dict[dish]):
            items_list = dict([(item['ingredient_name'], {'measure': item['measure'], 'quantity': int(item['quantity'])* persons})])
            if shop_list.get(item['ingredient_name']):
                extra_item = (int(shop_list[item['ingredient_name']]['quantity']) + int(items_list[item['ingredient_name']]['quantity']))
                shop_list[item['ingredient_name']]['quantity'] = extra_item
            else:
                shop_list.update(items_list)
    print(f"Для {persons} человек нам необходимо:")
    print(shop_list)

get_dishes(['Омлет', 'Запеченный картофель'], 2)
