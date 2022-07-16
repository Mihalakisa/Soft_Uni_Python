import math


def center_point(x, y):
    result = abs(x) + abs(y)
    return result


x1 = math.floor(float(input()))
y1 = math.floor(float(input()))
x2 = math.floor(float(input()))
y2 = math.floor(float(input()))

dist1 = center_point(x1, y1)
dist2 = center_point(x2, y2)

if dist1 <= dist2:
    print(f"({x1}, {y1})")
else:
    print(f"({x2}, {y2})")
