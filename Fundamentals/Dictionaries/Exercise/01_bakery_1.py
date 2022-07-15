products = input().split(' ')
bakery = dict()

for i in range(0, len(products), 2):
    key_product = products[i]
    value_product = int(products[i + 1])

    bakery[key_product] = value_product

print(bakery)
