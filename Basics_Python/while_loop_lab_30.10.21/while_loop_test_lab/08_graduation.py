student_name = input()
class_count = 1
bad_count = 0
sum_grade = 0

while True:
    if bad_count > 1:
        print(f"{student_name} has been excluded at {class_count} grade")
        break

    grade = float(input())

    if grade < 4:
        bad_count += 1
        continue

    sum_grade += grade
    if class_count == 12:
        average_grade = sum_grade / class_count
        print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
        break

    class_count += 1