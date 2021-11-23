from pprint import pprint
import os


def get_cook_book_from_file(file):
    """ Generate cook_book dict from file.txt """
    with open(file, 'r', encoding='UTF-8') as f:
        cook_book = dict()
        for recipe_name in f:
            recipe = recipe_name.strip()
            counter = int(f.readline())
            food_list = []
            for lines in range(counter):
                name, quantity, item = f.readline().strip().split("|")
                food_list.append(
                    {'ingredient_name': name.strip(), 'quantity': int(quantity), 'measure': item.strip()}
                )
            cook_book[recipe] = food_list
            f.readline()
        return cook_book


def get_shop_list_by_dishes(dishes, person_count, recipe_book='recipes.txt'):
    """ Counts the ingredients depending on person_count and selected dishes"""
    cook_book = get_cook_book_from_file(recipe_book)
    ingredient_dict = {}
    for recipe in dishes:
        if recipe in cook_book.keys():
            for food_dict in cook_book[recipe]:
                key = food_dict['ingredient_name']
                temp = food_dict['quantity'] * person_count
                temp_dict = {'measure': food_dict['measure'], 'quantity': temp}
                if key in ingredient_dict.keys():
                    exist_dict = ingredient_dict[key]
                    temp_dict['quantity'] += exist_dict['quantity']
                ingredient_dict[key] = temp_dict
    return ingredient_dict


def get_count_line_in_file(file):
    """ Simple counter for line in file """
    count_lines = 0
    with open(file, 'r', encoding='UTF-8') as f:
        for lines in f:
            count_lines += 1
    return count_lines


def generate_data_dict(files_dir):
    """ Find all files .txt inside files_dir and generate data_dict """
    data = {}
    file_list = []
    for files in os.listdir(files_dir):
        if files.endswith(".txt"):
            file_list.append(files)
    for file in file_list:
        path_file = os.path.join(files_dir, file)
        with open(path_file, 'r', encoding='UTF-8') as f:
            file_name = os.path.basename(path_file)
            properties = (get_count_line_in_file(path_file), f.read().strip())
            data[file_name] = properties
    return data


def sort_write_data_dict(data):
    """ Sort data_dict, create sorted_dict and write in file result.txt inside result_file folder """
    sorted_list = sorted(data.items(), key=lambda item: item[1][0])
    sorted_dict = {k: v for k, v in sorted_list}
    with open(os.path.join('result_file', 'result.txt'), 'w', encoding='UTF-8') as f:
        for k, v in sorted_dict.items():
            f.write(k + '\n')
            f.write(str(v[0]) + '\n')
            f.write(v[1] + '\n')
    return


# For test exercise 1:
# pprint(get_cook_book_from_file('recipes.txt'))

# For test exercise 2:
# pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))
pprint(get_shop_list_by_dishes(['Омлет', 'Омлет'], 2))

# For test exercise 3:
sort_write_data_dict(generate_data_dict('files'))

