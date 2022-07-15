n = int(input())
p1_count = 0
p2_count = 0
p3_count = 0

for i in range(1, n + 1):
    number = int(input())

    if number % 2 == 0:
        p1_count += 1
    if number % 3 == 0:
        p2_count += 1
    if number % 4 == 0:
        p3_count += 1

p1_percent = (p1_count / n) * 100
p2_percent = (p2_count / n) * 100
p3_percent = (p3_count / n) * 100
print(f"{p1_percent:.2f}%")
print(f"{p2_percent:.2f}%")
print(f"{p3_percent:.2f}%")