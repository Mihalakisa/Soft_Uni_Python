from collections import deque

order_quantity = int(input())
all_orders = deque([int(x) for x in input().split()])

print(max(all_orders))

while all_orders:
    if order_quantity >= int(all_orders[0]):
        order_quantity -= int(all_orders[0])
        all_orders.popleft()
    else:
        break

if all_orders:
    print(f"Orders left: {' '.join([str(x) for x in all_orders])}")
else:
    print('Orders complete')