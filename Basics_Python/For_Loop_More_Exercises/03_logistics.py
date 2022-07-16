number_of_cargo = int(input())
all_cargo = 0
sum_minibus = 0
sum_truck = 0
sum_train = 0
minibus_tonnage = 0
truck_tonnage = 0
train_tonnage = 0

for _ in range(number_of_cargo):
    cargo_tonnage = int(input())
    all_cargo += cargo_tonnage

    if cargo_tonnage <= 3:
        minibus_tonnage += cargo_tonnage
        sum_minibus = minibus_tonnage * 200
    elif 4 <= cargo_tonnage <= 11:
        truck_tonnage += cargo_tonnage
        sum_truck = truck_tonnage * 175
    elif cargo_tonnage >= 12:
        train_tonnage += cargo_tonnage
        sum_train = train_tonnage * 120

average_per_tonnage = (sum_minibus + sum_truck + sum_train) / all_cargo
minibus_percent = minibus_tonnage / all_cargo * 100
truck_percent = truck_tonnage / all_cargo * 100
train_percent = train_tonnage / all_cargo * 100

print(f'{average_per_tonnage:.2f}')
print(f'{minibus_percent:.2f}%')
print(f'{truck_percent:.2f}%')
print(f'{train_percent:.2f}%')