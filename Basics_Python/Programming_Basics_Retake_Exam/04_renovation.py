import math

wall_height = int(input())
wall_width = int(input())
percent_area_not_to_be_painted = int(input())

total_surface_area = wall_width * wall_height * 4
walls_to_paint = math.ceil(total_surface_area - (total_surface_area * (percent_area_not_to_be_painted / 100)))

while True:
    liter_paint = input()

    if liter_paint == 'Tired!':
        print(f"{walls_to_paint} quadratic m left.")
        break

    walls_to_paint -= int(liter_paint)

    if walls_to_paint < 0:
        print(f"All walls are painted and you have {abs(walls_to_paint)} l paint left!")
        break
    if walls_to_paint == 0:
        print("All walls are painted! Great job, Pesho!")
        break