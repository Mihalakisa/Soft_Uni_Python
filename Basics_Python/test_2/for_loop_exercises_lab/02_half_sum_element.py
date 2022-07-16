import sys

n = int(input())
max_number = -sys.maxsize
total_sum = 0

for i in range(n):
    number = int(input())

    if number > max_number:
        max_number = number

    total_sum += number

if total_sum - max_number == max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    diff = abs(max_number - (total_sum - max_number))
    print('No')
    print(f'Diff = {diff}')