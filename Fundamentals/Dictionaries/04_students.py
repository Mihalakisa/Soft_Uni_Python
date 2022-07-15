text = input()
courses = dict()

while ':' in text:

    data = text.split(':')  # (name, id, course) = text.split(':')
    name = data[0]          # <--- стават ненужни ако горното е написано
    id = data[1]            # <---------------
    course = data[2]        # <---------------

    if course not in courses.keys():
        courses[course] = dict()

    courses[course][id] = name

    text = input()

text = text.replace('_', ' ')

for id in courses[text]:
    print(f"{courses[text][id]} - {id}")
