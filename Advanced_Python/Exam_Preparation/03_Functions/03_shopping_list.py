def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."

    result = 0
    basket = 5
    final_res = ''

    for key in kwargs.keys():
        value_list = kwargs[key]
        price, quantity = value_list[0], value_list[1]
        result = price * quantity
        if result <= budget:
            budget -= result
            basket -= 1
            final_res += f"You bought {key} for {result:.2f} leva." + '\n'
        if basket == 0:
            break

    return final_res.strip()


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print()
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print()
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))