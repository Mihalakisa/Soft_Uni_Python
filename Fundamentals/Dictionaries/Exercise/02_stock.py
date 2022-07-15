products_list = input().split(' ')
bakery = {}

for i in range(0, len(products_list), 2):
    key_product = products_list[i]
    value_product = products_list[i + 1]
    bakery[key_product] = int(value_product)

searched_products = input().split(' ')

for product in searched_products:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
