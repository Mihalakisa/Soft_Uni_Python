price_of_baggage_over20kg = float(input())
kg_baggage = float(input())
days_to_travel = int(input())
number_of_baggage = int(input())

price = 0
if kg_baggage < 10:
    price = price_of_baggage_over20kg * 0.2
elif 10 <= kg_baggage <= 20:
    price = price_of_baggage_over20kg * 0.5
elif kg_baggage > 20:
    price = price_of_baggage_over20kg

if days_to_travel > 30:
    price = price + price * 0.1
elif 7 <= days_to_travel <= 30:
    price = price + price * 0.15
elif days_to_travel < 7:
    price = price + price * 0.4

total_price = price * number_of_baggage
print(f"The total price of bags is: {total_price:.2f} lv.")