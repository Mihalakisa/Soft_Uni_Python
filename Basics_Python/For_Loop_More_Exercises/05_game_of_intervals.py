number_of_moves = int(input())
result = 0
bottom_number = 0
low_number = 0
average_number = 0
great_number = 0
top_number = 0
invalid_number = 0

for i in range(number_of_moves):
    numbers_in_interval = int(input())

    if 0 <= numbers_in_interval <= 9:
        bottom_number += 1
        result += (numbers_in_interval * 20/100)
    elif 10 <= numbers_in_interval <= 19:
        low_number += 1
        result += (numbers_in_interval * 30/100)
    elif 20 <= numbers_in_interval <= 29:
        average_number += 1
        result += (numbers_in_interval * 40/100)
    elif 30 <= numbers_in_interval <= 39:
        great_number += 1
        result += 50
    elif 40 <= numbers_in_interval <= 50:
        top_number += 1
        result += 100
    else:
        invalid_number += 1
        result /= 2

bottom = bottom_number / number_of_moves * 100
low = low_number / number_of_moves * 100
average = average_number / number_of_moves * 100
great = great_number / number_of_moves * 100
top = top_number / number_of_moves * 100
invalid = invalid_number / number_of_moves * 100

print(f"{result:.2f}")
print(f"From 0 to 9: {bottom:.2f}%")
print(f"From 10 to 19: {low:.2f}%")
print(f"From 20 to 29: {average:.2f}%")
print(f"From 30 to 39: {great:.2f}%")
print(f"From 40 to 50: {top:.2f}%")
print(f"Invalid numbers: {invalid:.2f}%")