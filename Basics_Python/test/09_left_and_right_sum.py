n = int(input())

left_side = 0
right_side = 0

for i in range(1, n + 1):
    number = int(input())
    left_side += number

for i in range(1, n + 1):
    number = int(input())
    right_side += number

if left_side == right_side:
    print(f'Yes, sum = {left_side}')
else:
    sum = abs(left_side - right_side)
    print(f'No, diff = {sum}')