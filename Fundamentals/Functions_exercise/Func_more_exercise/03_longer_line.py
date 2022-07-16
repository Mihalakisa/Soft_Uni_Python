import math


def center_point(x, y):
    result = abs(x) + abs(y)
    return result


x1, y1 = math.floor(float(input())), math.floor(float(input()))
x2, y2 = math.floor(float(input())), math.floor(float(input()))
x3, y3 = math.floor(float(input())), math.floor(float(input()))
x4, y4 = math.floor(float(input())), math.floor(float(input()))

dist1 = center_point(x1, y1)
dist2 = center_point(x2, y2)
dist3 = center_point(x3, y3)
dist4 = center_point(x4, y4)

final_dist1 = dist1 + dist2
final_dist2 = dist3 + dist4

if final_dist1 <= final_dist2:
    print(f"({x4}, {y4})({x3}, {y3})")
else:
    print(f"({x2}, {y2})({x1}, {y1})")
