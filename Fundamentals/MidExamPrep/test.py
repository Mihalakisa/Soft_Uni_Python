def calculating(students, per_hour):
    hour = 1
    while True:
        if hour % 4 == 0:
            hour += 1

        if students > per_hour:
            students -= per_hour

        else:
            print(f"Time needed: {hour}h.")
            break

        hour += 1


all_per_hour = int(input()) + int(input()) + int(input())
students_count = int(input())
calculating(students_count, all_per_hour)
