budget = float(input())
extra_number = int(input())
clothing_per_extra = float(input())
decor = budget * 0.1
sum_for_cloth = extra_number * clothing_per_extra
if extra_number > 150:
    sum_for_cloth = sum_for_cloth - (sum_for_cloth * 0.1)
total_sum = decor + sum_for_cloth
remaining_sum = abs(budget - total_sum)

if budget >= total_sum:
    print("Action!")
    print(f"Wingard starts filming with {remaining_sum:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {remaining_sum:.2f} leva more.")