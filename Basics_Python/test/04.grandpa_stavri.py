number_of_days = int(input())
total_rakia = 0
degrees_per_liter = 0

for i in range(1, number_of_days +1):
    quantity_rakia = float(input())
    degrees = float(input())

    total_rakia += quantity_rakia
    degrees_per_liter += quantity_rakia * degrees

average_value = degrees_per_liter / total_rakia

print(f"Liter: {total_rakia:.2f}")
print(f"Degrees: {average_value:.2f}")

if average_value < 38:
    print("Not good, you should baking!")
elif 38 <= average_value <= 42:
    print("Super!")
elif average_value > 42:
    print("Dilution with distilled water!")