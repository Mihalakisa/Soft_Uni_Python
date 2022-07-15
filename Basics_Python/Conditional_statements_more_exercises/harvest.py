import math

x_vineyard_per_square_meter = int(input())
y_grapes_per_square_meter = float(input())
z_liters_wine = int(input())
number_of_workers = int(input())

total_grapes = x_vineyard_per_square_meter * y_grapes_per_square_meter
wine = 40/100 * total_grapes / 2.5

if wine >= z_liters_wine:
    total_wine = math.floor(wine)
    remaining_liters = math.ceil(wine - z_liters_wine)
    per_person = math.ceil(remaining_liters / number_of_workers)
    print(f'Good harvest this year! Total wine: {total_wine} liters.')
    print(f'{remaining_liters} liters left -> {per_person} liters per person.')
else:
    remaining = math.floor(z_liters_wine - wine)
    print(f'It will be a tough winter! More {remaining} liters wine needed.')