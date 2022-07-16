quantity_of_preparation = int(input()) * 750
remaining_preparation = quantity_of_preparation
number_of_plates = 0
number_of_pots = 0
count = 0

while True:
    number_of_dishes = input()
    count += 1
    if number_of_dishes == 'End':
        break

    if count % 3 == 0:
        number_of_pots += int(number_of_dishes)
        pots = int(number_of_dishes) * 15
        remaining_preparation -= pots
        if 0 > remaining_preparation:
            break

    if not count % 3 == 0:
        number_of_plates += int(number_of_dishes)
        plates = int(number_of_dishes) * 5
        remaining_preparation -= plates
        if 0 > remaining_preparation:
            break


if remaining_preparation < 0:
    print(f"Not enough detergent, {abs(remaining_preparation)} ml. more necessary!")
else:
    print("Detergent was enough!")
    print(f"{number_of_plates} dishes and {number_of_pots} pots were washed.")
    print(f"Leftover detergent {remaining_preparation} ml.")