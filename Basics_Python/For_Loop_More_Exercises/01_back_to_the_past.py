inherited_money = float(input())
year_to_live = int(input())
money_spend = 0
years = 17

for i in range(1800, year_to_live + 1):
    if i % 2 == 0:
        money_spend += 12000
    else:
        years += 2
        money_spend += 12000 + 50 * years

remaining_money = abs(inherited_money - money_spend)

if inherited_money >= money_spend:
    print(f"Yes! He will live a carefree life and will have {remaining_money:.2f} dollars left.")
else:
    print(f"He will need {remaining_money:.2f} dollars to survive.")