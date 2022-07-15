products = {}

command = input()

while command != 'statistics':
    text = command.split(': ')
    product = text[0]
    value = int(text[1])
    if product in products.keys():
        products[product] += value
    else:
        products[product] = value

    command = input()

total_products = len(products.keys())
total_quantity = sum(products.values())

print("Products in stock:")
for (product, value) in products.items():
    print(f"- {product}: {value}")
print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")
