number_of_bad_grades = int(input())
average_score = 0
bad_grades = 0
bad_grades_condition = False
number_of_problems = 0
while True:
    problem_name = input()
    if problem_name == 'Enough':
        break
    grade = int(input())

    average_score += grade
    last_problem = problem_name
    number_of_problems += 1
    if grade <= 4:
        bad_grades += 1
        if bad_grades == number_of_bad_grades:
            bad_grades_condition = True
            break

if bad_grades_condition:
    print(f"You need a break, {bad_grades} poor grades.")
else:
    average_score /= number_of_problems
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {number_of_problems}")
    print(f"Last problem: {last_problem}")