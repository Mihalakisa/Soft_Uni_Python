all_per_hour = int(input()) + int(input()) + int(input())
students_count = int(input())
hour = 0

while True:

    if students_count > 0:
        students_count -= all_per_hour
        hour += 1
    else:
        print(f"Time needed: {hour}h.")
        break

    if hour % 4 == 0:
        hour += 1
