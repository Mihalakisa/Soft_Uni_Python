food_list = input().split('!')
command = input()

while command != 'Go Shopping!':
    explode = command.split(' ')
    do_command = explode[0]
    product = explode[1]

    if do_command == 'Urgent':
        if product not in food_list:
            food_list.insert(0, product)

    elif do_command == 'Unnecessary':
        if product in food_list:
            food_list.remove(product)

    elif do_command == 'Correct':
        new_product = explode[2]
        if product in food_list:
            food_list = [item.replace(product, new_product) for item in food_list]

    elif do_command == 'Rearrange':
        if product in food_list:
            food_list.remove(product)
            food_list.append(product)

    command = input()

food_list = ', '.join(food_list)
print(food_list)
