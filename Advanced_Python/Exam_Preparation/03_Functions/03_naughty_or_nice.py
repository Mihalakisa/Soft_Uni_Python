def naughty_or_nice_list(kids, *args, **kwargs):
    nice_kids = []
    naughty_kids = []

    for command in args:
        num, status = command.split('-')
        num = int(num)
        name = None

        is_unique = False
        for kid_number, kid_name in kids:
            if num == kid_number and is_unique:
                is_unique = False
                break
            if num == kid_number:
                name = kid_name
                is_unique = True

        if is_unique:
            kids.remove((num, name))

            if status == 'Nice':
                nice_kids.append(name)
            else:
                naughty_kids.append(name)

    for name, status in kwargs.items():
        is_unique = False
        num = None

        for kid_number, kid_name in kids:
            if name == kid_name and is_unique:
                is_unique = False
                break
            if name == kid_name:
                is_unique = True
                num = kid_number

        if is_unique:
            kids.remove((num, name))
            if status == 'Nice':
                nice_kids.append(name)
            else:
                naughty_kids.append(name)

    not_found = [name for _, name in kids]

    result = ''

    if nice_kids:
        result += f"Nice: {', '.join(nice_kids)}\n"
    if naughty_kids:
        result += f"Naughty: {', '.join(naughty_kids)}\n"
    if not_found:
        result += f"Not found: {', '.join(not_found)}\n"

    return result.strip()


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print()
print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))

print()
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
