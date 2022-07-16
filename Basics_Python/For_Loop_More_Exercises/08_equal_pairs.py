import sys

number = int(input())
max = -sys.maxsize
min = sys.maxsize
num_one = 0
num_two = 0

for i in range(1, number + 1):
    value = int(input())
    num_one += value

    if num_one > max:
        max = num_one
    if num_one < min:
        min = num_one



if num_one == num_two:
    print(f"Yes, value={num_one}")
else:
    print(f"No, maxdiff={abs(min - max)}")