budget = float(input())
count = 0
all_cost = 0
diff = 0
num_count = 0

while True:
    product_name = input()

    if product_name == 'Stop':
        print(f"You bought {count} products for {all_cost:.2f} leva.")
        break

    product_price = float(input())

    count += 1

    if count % 3 == 0:
        product_price /= 2

    all_cost += product_price

    if all_cost > budget:
        diff = all_cost - budget
        print("You don't have enough money!")
        print(f"You need {diff:.2f} leva!")
        break