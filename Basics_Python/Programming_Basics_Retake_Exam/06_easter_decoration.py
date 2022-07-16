clients_number = int(input())
product_count = 0
total_cost = 0
all_cost = 0
price = 0

for i in range(1, clients_number + 1):
    while True:
        product = input()

        if product == 'Finish':
            if product_count % 2 == 0:
                total_cost = total_cost - (total_cost * 0.2)
                print(f"You purchased {product_count} items for {total_cost:.2f} leva.")
            else:
                print(f"You purchased {product_count} items for {total_cost:.2f} leva.")
            all_cost += total_cost
            price = 0
            total_cost = 0
            product_count = 0
            break

        product_count += 1

        if product == 'basket':
            price = 1.50
        elif product == 'wreath':
            price = 3.80
        elif product == 'chocolate bunny':
            price = 7

        total_cost += price

average_bill = all_cost / clients_number
print(f"Average bill per client is: {average_bill:.2f} leva.")