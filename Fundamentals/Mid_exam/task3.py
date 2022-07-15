# 03 Phone Shop
phones_list = input().split(', ')

while True:
    line = input()
    if line == 'End':
        print(', '.join(phones_list))
        break

    explode = line.split(' - ')
    command = explode[0]
    phone = explode[1]

    if command == 'Add':
        if phone not in phones_list:
            phones_list.append(phone)

    elif command == 'Remove':
        if phone in phones_list:
            phones_list.remove(phone)

    elif command == 'Bonus phone':
        phone_split = phone.split(':')
        old_phone = phone_split[0]
        new_phone = phone_split[1]
        if old_phone in phones_list:
            index_old_phone = phones_list.index(old_phone)
            phones_list.insert(index_old_phone + 1, new_phone)

    elif command == 'Last':
        if phone in phones_list:
            phones_list.remove(phone)
            phones_list.append(phone)
