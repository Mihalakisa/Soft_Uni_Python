width = int(input())
length = int(input())
height = int(input())
free_space = width * length * height
sum_boxes = 0

while True:
    number_of_boxes = input()

    if number_of_boxes == 'Done':
        break

    sum_boxes += int(number_of_boxes)

    if sum_boxes > free_space:
        break

diff = abs(sum_boxes - free_space)
if sum_boxes > free_space:
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"{diff} Cubic meters left.")