color_number = int(input())
total_points = 0
red = 0
orange = 0
yellow = 0
white = 0
black = 0
other = 0

for i in range(color_number):
    color = input()

    if color == 'red':
        total_points += 5
        red += 1
    elif color == 'orange':
        total_points += 10
        orange += 1
    elif color == 'yellow':
        total_points += 15
        yellow += 1
    elif color == 'white':
        total_points += 20
        white += 1
    elif color == 'black':
        total_points = int(total_points / 2)
        black += 1
    else:
        other += 1

print(f"Total points: {total_points}")
print(f"Red balls: {red}")
print(f"Orange balls: {orange}")
print(f"Yellow balls: {yellow}")
print(f"White balls: {white}")
print(f"Other colors picked: {other}")
print(f"Divides from black balls: {black}")