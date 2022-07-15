import math

group_size = int(input())
days = int(input())
sum_coins = 0

for day in range(1, days + 1):

    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5

    if day % 3 == 0:
        sum_coins -= (3 * group_size)
    if day % 5 == 0:
        sum_coins += (20 * group_size)
        if day % 3 == 0:
            sum_coins -= (2 * group_size)

    sum_coins += 50 - (2 * group_size)

coins = math.floor(sum_coins / group_size)
print(f"{group_size} companions received {coins} coins each.")
