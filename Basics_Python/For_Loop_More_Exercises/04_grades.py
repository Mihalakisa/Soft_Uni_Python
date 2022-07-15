number_of_students = int(input())
fail = 0
average = 0
great = 0
excellent = 0
all_grades = 0

for i in range(number_of_students):
    grade_from_exam = float(input())
    all_grades += grade_from_exam

    if 2.00 <= grade_from_exam <= 2.99:
        fail += 1
    elif 3.00 <= grade_from_exam <= 3.99:
        average += 1
    elif 4.00 <= grade_from_exam <= 4.99:
        great += 1
    elif grade_from_exam >= 5.00:
        excellent += 1

average_grades = all_grades / number_of_students
top_students = excellent / number_of_students * 100
great_students = great / number_of_students * 100
average_students = average / number_of_students * 100
fail_students = fail / number_of_students * 100

print(f"Top students: {top_students:.2f}%")
print(f"Between 4.00 and 4.99: {great_students:.2f}%")
print(f"Between 3.00 and 3.99: {average_students:.2f}%")
print(f"Fail: {fail_students:.2f}%")
print(f"Average: {average_grades:.2f}")