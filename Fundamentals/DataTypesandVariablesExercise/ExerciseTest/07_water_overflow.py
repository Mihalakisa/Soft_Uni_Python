num = int(input())
cap = 255
sum_liters = 0
is_true = True

for i in range(num):

    liters_water = int(input())
    cap -= liters_water
    if cap < 0:
        print(f"Insufficient capacity!")
        cap += liters_water
        is_true = False

    if is_true:
        sum_liters += liters_water

    is_true = True
print(sum_liters)
