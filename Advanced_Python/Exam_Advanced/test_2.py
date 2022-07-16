def shopping_cart(*args):
    soup_limit, pizza_limit, dessert_limit = 3, 4, 2
    soup_count, pizza_count, dessert_count = 0, 0, 0
    products = {}

    for i in range(len(args)):
        if args[i] == 'Stop':
            break

        meal = args[i][0]
        product = args[i][1]

        if pizza_count == pizza_limit and meal == 'Pizza':
            continue
        if soup_count == soup_limit and meal == 'Soup':
            continue
        if dessert_count == dessert_limit and meal == 'Dessert':
            continue

        if 'Soup' not in products:
            products['Soup'] = []
        if 'Pizza' not in products:
            products['Pizza'] = []
        if 'Dessert' not in products:
            products['Dessert'] = []

        if product not in products[meal]:
            products[meal].append(product)
            if meal == 'Pizza':
                pizza_count += 1
            elif meal == 'Soup':
                soup_count += 1
            elif meal == 'Dessert':
                dessert_count += 1

    if not products:
        return "No products in the cart!"

    else:
        sorted_items = sorted(products.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))

        result = ''

        length = {key: len(value) for key, value in products.items()}

        for key, value in sorted_items:
            if length[key] == 0:
                result += f"{key}:"
            else:
                result += f"{key}:" + '\n' ' - '
            sorted_values = sorted(value)
            result += '\n'' - '.join(sorted_values) + '\n'

        return result.strip()


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
print()
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print()
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
