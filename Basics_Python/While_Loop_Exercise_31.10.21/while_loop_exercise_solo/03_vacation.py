needed_money = float(input())
available_money = float(input())
days_count = 0
spend_count = 0

while True:
    operation = input()
    current_money = float(input())

    days_count += 1

    if operation == 'spend':
        spend_count += 1
        available_money -= current_money
        if available_money < 0:
            available_money = 0

    elif operation == 'save':
        spend_count = 0
        available_money += current_money
        if available_money >= needed_money:
            break

    if spend_count == 5:
        break

if spend_count == 5:
    print("You can't save the money.")
    print(f"{days_count}")
else:
    print(f"You saved the money for {days_count} days.")