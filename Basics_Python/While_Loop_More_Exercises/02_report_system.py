expect_to_collect_sum = int(input())
total_sum = 0
count = 0
total_cash = 0
total_card_cash = 0
count_cash = 0
count_card = 0

while True:
    product = input()
    count += 1

    if product == 'End':
        print("Failed to collect required money for charity.")
        break

    if not count % 2 == 0:
        if int(product) > 100:
            print("Error in transaction!")
        else:
            total_cash += int(product)
            count_cash += 1
            print("Product sold!")

    if count % 2 == 0:
        if int(product) < 10:
            print("Error in transaction!")
        else:
            total_card_cash += int(product)
            count_card += 1
            print("Product sold!")

    total_sum = total_cash + total_card_cash
    if expect_to_collect_sum <= total_sum:
        print(f"Average CS: {(total_cash / count_cash):.2f}")
        print(f"Average CC: {(total_card_cash / count_card):.2f}")
        break