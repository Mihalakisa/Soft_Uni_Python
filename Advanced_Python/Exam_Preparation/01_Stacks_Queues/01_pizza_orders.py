from collections import deque

pizza_orders = deque([int(x) for x in input().split(', ')])
employees = [int(x) for x in input().split(', ')]

pizza_counter = 0
while pizza_orders and employees:
    pizza_order = pizza_orders.popleft()
    if pizza_order > 10 or pizza_order <= 0:
        continue
    employee = employees.pop()

    if pizza_order <= employee:
        pizza_counter += pizza_order
    elif pizza_order > employee:
        pizza_order -= employee
        pizza_counter += employee
        pizza_orders.appendleft(pizza_order)

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizza_counter}")
    print(f"Employees: {', '.join(str(x) for x in employees)}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizza_orders)}")
