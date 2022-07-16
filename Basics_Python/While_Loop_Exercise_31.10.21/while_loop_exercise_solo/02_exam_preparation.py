bad_grades = int(input())
sum_grades = 0
count_grades = 0
count_task = 0
task = ''

while True:
    name_of_task = input()
    if name_of_task == 'Enough':
        break
    grades = int(input())

    sum_grades += grades
    count_task += 1
    task = name_of_task
    if grades <= 4:
        count_grades += 1
        if count_grades == bad_grades:
            break

if count_grades == bad_grades:
    print(f"You need a break, {bad_grades} poor grades.")
else:
    average_sum = sum_grades / count_task
    print(f"Average score: {average_sum:.2f}")
    print(f"Number of problems: {count_task}")
    print(f"Last problem: {task}")