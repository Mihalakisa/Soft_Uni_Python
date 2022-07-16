voucher_value = int(input())
movie = 0
product = 0
remaining = voucher_value
count_movie = 0
count_product = 0

while True:
    purchase = input()

    if purchase == 'End':
        break
    if len(purchase) > 8:
        movie = ord(purchase[0]) + ord(purchase[1])
        if remaining < movie:
            break
        else:
            remaining -= movie
        count_movie += 1

    elif len(purchase) <= 8:
        product = ord(purchase[0])
        if remaining < product:
            break
        else:
            remaining -= product
        count_product += 1

print(count_movie)
print(count_product)
