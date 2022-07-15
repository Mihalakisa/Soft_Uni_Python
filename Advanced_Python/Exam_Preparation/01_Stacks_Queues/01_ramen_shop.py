from collections import deque

ramens = [int(x) for x in input().split(', ')]
customers = deque([int(x) for x in input().split(', ')])

while ramens and customers:
    current_ramen = ramens.pop()
    current_customer = customers.popleft()

    if current_ramen > current_customer:
        current_ramen -= current_customer
        ramens.append(current_ramen)

    elif current_customer > current_ramen:
        current_customer -= current_ramen
        customers.appendleft(current_customer)

if ramens:
    print("Great job! You served all the customers.")
    print(f"Bowls of ramen left: {', '.join(str(x) for x in ramens)}")

elif customers:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")
else:
    print("Great job! You served all the customers.")