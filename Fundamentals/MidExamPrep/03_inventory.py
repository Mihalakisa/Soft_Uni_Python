items_list = input().split(', ')
combine = ''

while True:
    line = input()
    if line == 'Craft!':
        items_list = ', '.join(items_list)
        print(items_list)
        break

    explode = line.split(' - ')
    command = explode[0]
    item = explode[1]

    if command == 'Collect':
        if item not in items_list:
            items_list.append(item)

    elif command == 'Drop':
        if item in items_list:
            items_list.remove(item)

    elif command == 'Combine Items':
        combine = item.split(':')
        old_item = combine[0]
        new_item = combine[1]
        if old_item in items_list:
            index_old_element = items_list.index(old_item)
            items_list.insert(index_old_element + 1, new_item)

    elif command == 'Renew':
        if item in items_list:
            items_list.remove(item)
            items_list.append(item)
