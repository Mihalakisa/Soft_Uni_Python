t_shirt_price = float(input())
needed_price = float(input())

shorts_price = t_shirt_price * 0.75
socks_price = shorts_price * 0.20
buttons_price = (t_shirt_price + shorts_price) * 2
total_price = t_shirt_price + shorts_price + socks_price + buttons_price
total_price = total_price - (total_price * 0.15)

if total_price >= needed_price:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_price:.2f} lv.")
else:
    diff = abs(total_price - needed_price)
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {diff:.2f} lv. more.")