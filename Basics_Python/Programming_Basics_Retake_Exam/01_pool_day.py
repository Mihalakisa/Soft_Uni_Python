import math

number_of_ppl = int(input())
entrance_tax = float(input())
deck_chair_tax = float(input())
umbrella_tax = float(input())

entrance_tax = entrance_tax * number_of_ppl
needed_deck_chairs = math.ceil(number_of_ppl * 0.75) * deck_chair_tax
needed_umbrellas = math.ceil(number_of_ppl * 0.5) * umbrella_tax
all_sum = entrance_tax + needed_deck_chairs + needed_umbrellas

print(f"{all_sum:.2f} lv.")
