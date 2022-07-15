x = float(input())
y = float(input())
h = float(input())
# Стени
side_wall = x * y
window = 1.5 * 1.5
both_sides = 2 * side_wall - 2 * window
back_wall = x * x
entrance = 1.2 * 2
front_back_wall = 2 * back_wall - entrance
total_area_wall = front_back_wall + both_sides
green_paint = total_area_wall / 3.4

# Покрив
two_rectangles_on_the_roof = 2 * (x * y)
two_triangles = 2 * (x * h / 2)
total_area_roof = two_rectangles_on_the_roof + two_triangles
red_paint = total_area_roof / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")