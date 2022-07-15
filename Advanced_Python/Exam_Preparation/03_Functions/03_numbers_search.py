def numbers_searching(*args):
    check_list = []
    duplicate_numbers = []
    for i in args:
        if i not in check_list:
            check_list.append(i)
        else:
            if i not in duplicate_numbers:
                duplicate_numbers.append(i)

    check_list = sorted(check_list)
    duplicate_numbers = sorted(duplicate_numbers)
    searched_number = 0

    for i in check_list:
        if i + 1 not in check_list:
            searched_number = i + 1
            break

    return [searched_number, duplicate_numbers]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print()
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print()
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
