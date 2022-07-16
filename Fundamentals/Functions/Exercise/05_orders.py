def calculate(product, num):
    if product == "coffee":
        return 1.5 * num
    elif product == "coke":
        return 1.4 * num
    elif product == "water":
        return 1 * num
    elif product == "snacks":
        return 2 * num


current_product = input()
quantity = int(input())

price = calculate(current_product, quantity)
print(f"{price:.2f}")
