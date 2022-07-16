from collections import deque

customers = deque([int(x) for x in input().split(', ')])
taxis = [int(x) for x in input().split(', ')]
total_time = 0

while customers and taxis:
    customer = customers[0]
    taxi = taxis[-1]

    if taxi < customer:
        taxis.pop()
    else:
        total_time += customer
        customers.popleft()
        taxis.pop()

if customers:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")
else:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
