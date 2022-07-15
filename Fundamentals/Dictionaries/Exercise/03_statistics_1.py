products = dict()
command = input()

while command != 'statistics':
    data = command.split(': ')
    product = data[0]
    value = int(data[1])

    if product not in products:
        products[product] = value
    else:
        products[product] += value

    command = input()

total_products = len(products.keys())
total_quantity = sum(products.values())

print("Products in stock:")
for product in products:
    print(f"- {product}: {products[product]}")
print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")
