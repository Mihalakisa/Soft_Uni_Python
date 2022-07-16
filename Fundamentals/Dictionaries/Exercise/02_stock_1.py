products = input().split(' ')
bakery = dict()

for i in range(0, len(products), 2):
    key_product = products[i]
    value_product = int(products[i + 1])

    bakery[key_product] = value_product

searched_products = input().split(' ')

for product in searched_products:
    if product not in bakery.keys():
        print(f"Sorry, we don't have {product}")
    else:
        print(f"We have {bakery[product]} of {product} left")
