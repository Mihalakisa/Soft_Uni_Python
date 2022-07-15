nylon = int(input())
price_nylon = (nylon + 2) * 1.50
paint = int(input())
price_paint = (paint + 0.1) * 14.50
paint_thinner = int(input()) * 5.00
work_hours = int(input())
price_mats = price_nylon + price_paint + paint_thinner + 0.40
price_workers = (price_mats * 0.3) * work_hours
final_price = price_mats + price_workers

print(final_price)