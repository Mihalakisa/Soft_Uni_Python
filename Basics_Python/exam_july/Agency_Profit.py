air_agency = str(input())
adult_tickets = int(input())
kid_tickets = int(input())
net_worth_adult_t = float(input())
service_fee = float(input())

net_worth_kid_t = net_worth_adult_t - (net_worth_adult_t * 0.7)
adult_ticket_and_fee = net_worth_adult_t + service_fee
kid_ticket_and_fee = net_worth_kid_t + service_fee
all_ticket_price = (kid_tickets * kid_ticket_and_fee) + (adult_tickets * adult_ticket_and_fee)
profit = all_ticket_price * 0.2
profit = (f"{profit:.2f}")

print(f"The profit of your agency from {air_agency} tickets is {profit} lv.")