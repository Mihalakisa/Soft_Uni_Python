products = input().split(' ')
bakery = {}

for i in range(0, len(products), 2):
    key_product = products[i]
    value_product = products[i + 1]

    bakery[key_product] = int(value_product)

print(bakery)
