days = int(input())
hours = int(input())
cost = 0
total = 0

for day in range(1, days + 1):
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            cost += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            cost += 1.25
        else:
            cost += 1

    total += cost
    print(f"Day: {day} - {cost:.2f} leva")
    cost = 0
print(f"Total: {total:.2f} leva")
