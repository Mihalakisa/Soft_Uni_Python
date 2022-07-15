strawberry_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberry_kg = float(input())

raspberry_price = strawberry_price / 2
oranges_price = raspberry_price - (0.4 * raspberry_price)
bananas_price = raspberry_price - (0.8 * raspberry_price)
sum_raspberry = raspberry_price * raspberries_kg
sum_oranges = oranges_price * oranges_kg
sum_bananas = bananas_price * bananas_kg
sum_strawberry = strawberry_price * strawberry_kg
total_sum = sum_strawberry + sum_bananas + sum_oranges + sum_raspberry
print(f"{total_sum:.2f}")