courses_dict = {}

while True:
    info = input()

    if info == 'end':
        break

    info = info.split(' : ')
    course = info[0]
    name = info[1]

    if course not in courses_dict.keys():
        courses_dict[course] = []
    courses_dict[course].append(name)

for course in courses_dict.keys():
    print(f"{course}: {len(courses_dict[course])}")
    for name in courses_dict[course]:
        print(f"-- {name}")
