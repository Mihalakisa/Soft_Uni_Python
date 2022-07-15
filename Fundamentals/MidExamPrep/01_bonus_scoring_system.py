students = int(input())
lectures = int(input())
bonus = int(input())
total_bonus = 0
best_student = 0
max_bonus = 0

for student in range(students):
    student_attendances = int(input())

    total_bonus = (student_attendances / lectures) * (5 + bonus)

    if total_bonus > max_bonus:
        max_bonus = total_bonus
        best_student = student_attendances

print(f"Max Bonus: {round(max_bonus)}.")
print(f"The student has attended {best_student} lectures.")
