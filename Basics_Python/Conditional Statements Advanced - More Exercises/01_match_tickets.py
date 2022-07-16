budget = float(input())
status = input()
number_of_ppl = int(input())
costs = 0
ticket_cost = 0

if status == "VIP":
    ticket_vip = 499.99
    if 1 <= number_of_ppl <= 4:
        costs = budget - (budget * 0.75)
        ticket_cost = ticket_vip * number_of_ppl
    elif 5 <= number_of_ppl <= 9:
        costs = budget - (budget * 0.6)
        ticket_cost = ticket_vip * number_of_ppl
    elif 10 <= number_of_ppl <= 24:
        costs = budget - (budget * 0.5)
        ticket_cost = ticket_vip * number_of_ppl
    elif 25 <= number_of_ppl <= 49:
        costs = budget - (budget * 0.4)
        ticket_cost = ticket_vip * number_of_ppl
    elif 50 <= number_of_ppl:
        costs = budget - (budget * 0.25)
        ticket_cost = ticket_vip * number_of_ppl

elif status == "Normal":
    ticket_normal = 249.99
    if 1 <= number_of_ppl <= 4:
        costs = budget - (budget * 0.75)
        ticket_cost = ticket_normal * number_of_ppl
    elif 5 <= number_of_ppl <= 9:
        costs = budget - (budget * 0.6)
        ticket_cost = ticket_normal * number_of_ppl
    elif 10 <= number_of_ppl <= 24:
        costs = budget - (budget * 0.5)
        ticket_cost = ticket_normal * number_of_ppl
    elif 25 <= number_of_ppl <= 49:
        costs = budget - (budget * 0.4)
        ticket_cost = ticket_normal * number_of_ppl
    elif 50 <= number_of_ppl:
        costs = budget - (budget * 0.25)
        ticket_cost = ticket_normal * number_of_ppl

diff = abs(costs - ticket_cost)
if ticket_cost < costs:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')