number = input().split(", ")
max_numbers = 0

while len(number) > 0:
    temp_list = []
    max_numbers += 10

    for x in number:
        if int(x) <= max_numbers:
            temp_list.append(int(x))

    [number.remove(str(x)) for x in temp_list]
    print(f"Group of {max_numbers}'s: {temp_list}")
