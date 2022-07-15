import math

needed_hours = int(input())
days = int(input())
number_of_employees = int(input())

work_hours = (days - days * 0.1) * 8
extra_hours = number_of_employees * (2 * days)
total_hours = math.floor(work_hours + extra_hours)

if total_hours >= needed_hours:
    diff = total_hours - needed_hours
    print(f"Yes!{diff} hours left.")
else:
    diff = abs(total_hours - needed_hours)
    print(f"Not enough time!{diff} hours needed.")