price_mackerel_kg = float(input())
price_sprat_kg = float(input())
price_bonito_kg = float(input())
price_horse_mackerel_kg = float(input())
price_mussels_kg = int(input())

price_of_bonito = price_mackerel_kg + price_mackerel_kg * 0.6
final_bonito = price_of_bonito * price_bonito_kg
price_of_horse_mackerel = price_sprat_kg + price_sprat_kg * 0.8
final_horse_mackerel = price_of_horse_mackerel * price_horse_mackerel_kg
final_mussels = price_mussels_kg * 7.50
bill = final_bonito + final_horse_mackerel + final_mussels

print(f"{bill:.2f}")