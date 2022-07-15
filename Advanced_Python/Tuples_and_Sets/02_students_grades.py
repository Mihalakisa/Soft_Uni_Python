def avg(values):
    return sum(values) / len(values)


n = int(input())

students_strings = [input() for _ in range(n)]

students_grades = {}

for student_string in students_strings:
    student, grade_string = student_string.split(' ')
    if student not in students_grades:
        students_grades[student] = []
    students_grades[student].append(float(grade_string))

for student, grades in students_grades.items():
    grades_avg = avg(grades)
    grades_formatted = ' '.join(f"{grade:.2f}" for grade in grades)
    grades_avg_formatted = f"{grades_avg:.2f}"
    print(f"{student} -> {grades_formatted} (avg: {grades_avg})")
