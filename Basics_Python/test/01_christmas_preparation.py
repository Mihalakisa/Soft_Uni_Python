number_wrapping_paper = int(input())
number_rolls_of_cloth = int(input())
liters_of_glue = float(input())
percent_discount = int(input())

wrapping_paper_price = number_wrapping_paper * 5.80
rolls_of_cloth_price = number_rolls_of_cloth * 7.20
glue_price = liters_of_glue * 1.20
all_mats_price = wrapping_paper_price + rolls_of_cloth_price + glue_price
discount_price = all_mats_price - (all_mats_price * (percent_discount / 100))

print(f"{discount_price:.3f}")