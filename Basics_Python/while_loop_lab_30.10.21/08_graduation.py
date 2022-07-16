name_of_student = str(input())
class_grade = 1
failures = 0
sum_year_grade = 0

while True:
    if failures > 1:
        print(f"{name_of_student} has been excluded at {class_grade} grade")
        break

    year_grades = float(input())

    if year_grades < 4:
        failures += 1
        continue

    sum_year_grade += year_grades
    if class_grade == 12:
        average_grade = sum_year_grade / class_grade
        print(f"{name_of_student} graduated. Average grade: {average_grade:.2f}")
        break
    class_grade += 1