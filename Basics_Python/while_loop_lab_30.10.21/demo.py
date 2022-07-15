name = str(input())
class_grade = 1
sum_n_grade = 0
average_grade = 0
failures = 0

while True:
    if failures > 1:
        print(f"{name} has been excluded at {class_grade} grade")
        break

    n_grade = float(input())

    if n_grade < 4:
        failures += 1
        continue

    sum_n_grade += n_grade

    if class_grade == 12:
        average_grade = sum_n_grade / class_grade
        print(f"{name} graduated. Average grade: {average_grade:.2f}")
        break
    class_grade += 1