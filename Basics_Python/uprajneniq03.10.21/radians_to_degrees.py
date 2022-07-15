# 1. Променлива за радиани (float) -> въвежда
# 2. Пресмятане на градуси: градуси = радиани * 180 / пи
# 3. Отпечатваме градуси
import math
radians = float(input())
decrees = radians * 180 / math.pi
print(decrees)