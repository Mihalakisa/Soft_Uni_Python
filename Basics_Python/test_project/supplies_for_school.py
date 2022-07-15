pen_package = int(input())
price_pen = pen_package * 5.80
markers_package = int(input())
price_markers = markers_package * 7.20
liters_of_prep = int(input())
price_liters = liters_of_prep * 1.20
discount = int(input())
percent_discount = discount / 100

overall_price = price_pen + price_markers + price_liters
final_price = overall_price - (overall_price * percent_discount)

print(final_price)