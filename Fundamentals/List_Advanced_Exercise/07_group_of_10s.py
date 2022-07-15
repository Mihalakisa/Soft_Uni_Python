numbers_list = list(map(int, input().split(', ')))
max_number = max(numbers_list)
group = 0
max_group = 10
sorted_list = []

while True:
    for num in numbers_list:
        if group < num <= max_group:
            sorted_list.append(num)
    print(f"Group of {max_group}'s: {sorted_list}")
    sorted_list.clear()

    if max_group >= max_number:
        break

    group += 10
    max_group += 10
