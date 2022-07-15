import sys

n = int(input())
max = -sys.maxsize
sum = 0

for num in range(1, n + 1):
    number = int(input())

    if number > max:
        max = number

    sum += number

if sum - max == max:
    print("Yes")
    print(f"Sum = {max}")
else:
    print("No")
    print(f"Diff = {abs(max - (sum - max))}")