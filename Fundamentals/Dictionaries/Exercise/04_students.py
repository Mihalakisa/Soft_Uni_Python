text = input()
courses = {}

while ':' in text:
    data = text.split(':')
    name = data[0]
    student_id = data[1]
    course = data[2]

    if course not in courses:
        courses[course] = {}
    courses[course][student_id] = name

    text = input()

text = text.replace('_', ' ')

for id in courses[text]:
    print(f"{courses[text][id]} - {id}")
