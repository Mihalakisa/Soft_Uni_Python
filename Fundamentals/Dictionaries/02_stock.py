data = input().split(" ")
search_products = input().split(" ")
bakery = dict()

for i in range(0, len(data), 2):
    food = data[i]
    quantity = data[i+1]
    bakery[food] = int(quantity)

for product in search_products:
    if product in bakery.keys():
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")