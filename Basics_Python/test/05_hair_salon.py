day_target = int(input())
profit = 0

while True:
    operation = input()

    if operation == 'closed':
        diff = abs(profit - day_target)
        print(f"Target not reached! You need {diff}lv. more.")
        print(f"Earned money: {profit}lv.")
        break

    if operation == 'haircut':
        operation = input()
        if operation == 'mens':
            price = 15
            profit += price
        elif operation == 'ladies':
            price = 20
            profit += price
        elif operation == 'kids':
            price = 10
            profit += price

    elif operation == 'color':
        operation = input()
        if operation == 'touch up':
            price = 20
            profit += price
        elif operation == 'full color':
            price = 30
            profit += price

    if profit >= day_target:
        print("You have reached your target for the day!")
        print(f"Earned money: {profit}lv.")
        break