counter = int(input())
grades_dict = {}

for i in range(counter):
    name = input()
    grade = float(input())

    if name not in grades_dict.keys():
        grades_dict[name] = []
    grades_dict[name].append(grade)

for i in grades_dict:
    average_grade = sum(grades_dict[i]) / len(grades_dict[i])
    if float(average_grade) >= 4.5:
        print(f"{i} -> {average_grade:.2f}")