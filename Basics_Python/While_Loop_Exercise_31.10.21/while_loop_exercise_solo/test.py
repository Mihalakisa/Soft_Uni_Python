number_bad_grades = int(input())
task = 0
average_score = 0
count = 0
grade_condition = False

while True:
    task_name = input()
    if task_name == 'Enough':
        break
    grade = int(input())

    task += 1
    average_score += grade
    last_problem = task_name

    if grade <= 4:
        count += 1
        if number_bad_grades == count:
            grade_condition = True
            break

if grade_condition:
    print(f"You need a break, {number_bad_grades} poor grades.")
else:
    average_score /= task
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {task}")
    print(f"Last problem: {last_problem}")